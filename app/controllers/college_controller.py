from flask import Blueprint, render_template, jsonify, request, g
from app.models.college_model import CollegeModel

college_blueprint = Blueprint('college', __name__)

@college_blueprint.route('/api/tabColleges', methods=['GET'])
def api_display_tab_college():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        response = CollegeModel().count_rows()
        if response['response'] > 0:
            colleges = CollegeModel().list_all()
            headers = ["Code", "College"]
            data = {'content': render_template('content/table_view.html', headers=headers, rows=colleges['response'])}
            return jsonify(data)
        else:
            data = {'content': render_template('content/warning_view.html', description="", button_text="")}
            return jsonify(data)
    else:
        return jsonify({'error': 'Unwanted request header'}), 400

@college_blueprint.route('/api/college/create', methods=['POST'])
def api_create_college():
    request_body = request.get_json()
    if request_body:
        code = str(request_body['code']) 
        name = str(request_body['name'])
        colleges = CollegeModel().insert(code, name)
        return jsonify(response = colleges), 201
    else:
        return jsonify({'error': 'Invalid request data'}), 400

@college_blueprint.route('/api/college/read/<code>', methods=['GET'])
def api_read_college(code):
    college = CollegeModel().read(code)
    return jsonify(college), 201

@college_blueprint.route('/api/college/update', methods=['POST'])
def api_update_college():
    request_body = request.get_json()
    if request_body:
        code = str(request_body['code']) 
        name = str(request_body['name'])
        new_code = str(request_body['new_code'])
        new_name = str(request_body['new_name'])
        college = CollegeModel().update(code, name, new_code, new_name)
        return jsonify(response = college), 201
    else:
        return jsonify({'error': 'Invalid request data'}), 400

@college_blueprint.route('/api/college/delete', methods=['POST'])
def api_delete_college():
    request_body = request.get_json()
    if request_body:
        code = str(request_body['code'])
        college = CollegeModel().delete(code)
        return jsonify(response = college), 201
    else:
        return jsonify({'error': 'Invalid request data'}), 400

@college_blueprint.route('/api/college/list', methods=['GET'])
def api_get_colleges():
    colleges = CollegeModel().list_all()
    return jsonify(colleges), 201
