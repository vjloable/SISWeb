from flask import Blueprint, render_template, jsonify, request, g
from app.models.college_model import CollegeModel
college_blueprint = Blueprint('college', __name__)

@college_blueprint.route('/api/college', methods=['GET'])
def api_get_college():
    colleges = CollegeModel().list_all()
    return jsonify(colleges), 201

@college_blueprint.route('/api/college', methods=['POST'])
def api_add_college():
    add_college_request = request.get_json()
    if add_college_request:
        print("add_college_request: {}".format(add_college_request))
        code = str(add_college_request['code']) 
        name = str(add_college_request['name'])
        colleges = CollegeModel().insert(code, name)
        print("colleges response: {}".format(colleges))
        return jsonify(response = colleges), 201
    else:
        return jsonify({'error': 'Invalid request data'}), 400