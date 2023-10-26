from flask import Blueprint, request
from app.models.college_model import CollegeModel
from app.views.college_view import CollegeView

college_blueprint = Blueprint('college', __name__)

@college_blueprint.route('/api/tabColleges', methods=['GET'])
def api_display_tab_college():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        response = CollegeModel.count_rows()
        if response['response'] > 0:
            model_response = CollegeModel.list_all()
            render_model = model_response['response']
            return CollegeView.renderTableAsJSON(render_model)
        else:
            return CollegeView.renderNoDataAsJSON()
    else:
        return CollegeView.setPayloadToJSON(403)

@college_blueprint.route('/college/create', methods=['GET'])
def create_college():
    return CollegeView.renderCreateFormAsView()

@college_blueprint.route('/api/college/create', methods=['POST'])
def api_create_college():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        request_body = request.get_json()
        if request_body:
            code = str(request_body['code']) 
            name = str(request_body['name'])
            model_response = CollegeModel.insert(code, name)
            return CollegeView.setPayloadToJSON(201, payload=model_response)
        else:
            return CollegeView.setPayloadToJSON(400)
    else:
        return CollegeView.setPayloadToJSON(403)
    

@college_blueprint.route('/api/college/read/<code>', methods=['GET'])
def api_read_college(code):
    model_response = CollegeModel.read(code)
    return CollegeView.setPayloadToJSON(201, payload=model_response)

@college_blueprint.route('/api/college/update', methods=['POST'])
def api_update_college():
    request_body = request.get_json()
    if request_body:
        code = str(request_body['code']) 
        new_code = str(request_body['new_code'])
        new_name = str(request_body['new_name'])
        model_response = CollegeModel.update(code, new_code, new_name)
        return CollegeView.setPayloadToJSON(201, payload=model_response)
    else:
        return CollegeView.setPayloadToJSON(400)

@college_blueprint.route('/api/college/delete', methods=['POST'])
def api_delete_college():
    request_body = request.get_json()
    if request_body:
        code = str(request_body['code'])
        model_response = CollegeModel.delete(code)
        return jsonify(**model_response), 201
    else:
        return CollegeView.setPayloadToJSON(400)

@college_blueprint.route('/api/college/list', methods=['GET'])
def api_get_colleges():
    model_response = CollegeModel.list_all()
    return CollegeView.setPayloadToJSON(201, payload=model_response)
