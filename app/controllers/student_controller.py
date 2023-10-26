from flask import Blueprint, request
from app.models.student_model import StudentModel
from app.views.student_view import StudentView

student_blueprint = Blueprint('student', __name__)

@student_blueprint.route('/api/tabStudents', methods=['GET'])
def api_display_tab_student():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        response = StudentModel.count_rows()
        if response['response'] > 0:
            model_response = StudentModel.list_all()
            render_model = model_response['response']
            return StudentView.renderTableAsJSON(render_model)
        else:
            return StudentView.renderNoDataAsJSON()
    else:
        return StudentView.setPayloadToJSON(403)

@student_blueprint.route('/student/create', methods=['GET'])
def create_student():
    return StudentView.renderCreateFormAsView()

@student_blueprint.route('/api/student/create', methods=['POST'])
def api_create_student():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':    
        request_body = request.get_json()
        if request_body:
            student_id = str(request_body['student_id'])
            firstname = str(request_body['firstname'])
            lastname = str(request_body['lastname'])
            course_id = str(request_body['course_id'])
            year = str(request_body['year'])
            gender = str(request_body['gender'])
            model_response = StudentModel.insert(id, firstname, lastname, course_id, year, gender)
            return StudentView.setPayloadToJSON(201, payload=model_response)
        else:
            return StudentView.setPayloadToJSON(400)
    else:
        return CollegeView.setPayloadToJSON(403)

@student_blueprint.route('/api/student/read/<code>', methods=['GET'])
def api_read_student(code):
    model_response = StudentModel.read(code)
    return StudentView.setPayloadToJSON(201, payload=model_response)

@student_blueprint.route('/api/student/update', methods=['POST'])
def api_update_student():
    request_body = request.get_json()
    if request_body:
        student_id = str(request_body['student_id'])
        new_id = str(request_body['new_student_id'])
        new_firstname = str(request_body['new_firstname'])
        new_lastname = str(request_body['new_lastname'])
        new_course_id = str(request_body['new_course_id'])
        new_year = str(request_body['new_year'])
        new_gender = str(request_body['new_gender'])
        model_response = StudentModel.update(student_id, new_id, new_firstname, new_lastname, new_course_id, new_year, new_gender)
        return StudentView.setPayloadToJSON(201, payload=model_response)
    else:
        return StudentView.setPayloadToJSON(400)

@student_blueprint.route('/api/student/delete', methods=['POST'])
def api_delete_student():
    request_body = request.get_json()
    if request_body:
        student_id = str(request_body['student_id'])
        model_response = StudentModel.delete(student_id)
        return jsonify(**model_response), 201
    else:
        return StudentView.setPayloadToJSON(400)

@student_blueprint.route('/api/student/list', methods=['GET'])
def api_get_students():
    model_response = StudentModel.list_all()
    return StudentView.setPayloadToJSON(201, payload=model_response)
