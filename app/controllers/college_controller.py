from flask import Blueprint, render_template, jsonify, request

college_blueprint = Blueprint('college', __name__)

@college_blueprint.route('/college')
def get_college():
    return render_template('college.html')

@college_blueprint.route('/api/college', methods=['GET'])
def api_get_college():
    # call college model method to get colleges
    college_list = []
    return jsonify(college_list)

@college_blueprint.route('/api/college', methods=['POST'])
def api_add_college():
    add_college_request = request.get_json()
    if add_college_request:
        # call college model method to add a college
        return jsonify(college.to_dict()), 201
    else:
        return jsonify({'error': 'Invalid request data'}), 400