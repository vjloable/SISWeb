from flask import Blueprint, render_template, jsonify, request, g
from app.models.college_model import CollegeModel

college_blueprint = Blueprint('college', __name__)

@college_blueprint.route('/api/tabColleges', methods=['GET'])
def display_tab_college():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        response = CollegeModel().count_rows()
        if response['response'] > 0:
            data = {'content': render_template('content/colleges_hasdata.html')}
            return jsonify(data)
        else:
            data = {'content': render_template('content/colleges_nodata.html')}
            return jsonify(data)
    else:
        return jsonify({'error': 'Unwanted request header'}), 400

@college_blueprint.route('/api/college', methods=['GET'])
def api_get_college():
    colleges = CollegeModel().list_all()
    return jsonify(colleges), 201

@college_blueprint.route('/api/college', methods=['POST'])
def api_add_college():
    add_college_request = request.get_json()
    if add_college_request:
        code = str(add_college_request['code']) 
        name = str(add_college_request['name'])
        colleges = CollegeModel().insert(code, name)
        return jsonify(response = colleges), 201
    else:
        return jsonify({'error': 'Invalid request data'}), 400