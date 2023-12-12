from flask import Blueprint, request, session
from flask_session import Session
from app.models.student_model import StudentModel
from app.views.student_view import StudentView
from app.services.cloud_service import CloudService

student_blueprint = Blueprint('student', __name__)

@student_blueprint.route('/api/tabStudents', methods=['GET'])
def api_display_tab_student():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        results = StudentModel.count_rows()
        if results['results'] > 0:
            model_response = StudentModel.list_all()
            render_model = model_response['results']
            return StudentView.renderTableAsJSON(render_model)
        else:
            return StudentView.renderNoDataAsJSON()
    else:
        return StudentView.setPayloadToJSON(403)

@student_blueprint.route('/student/create', methods=['GET'])
def create_student():
    return StudentView.renderCreateFormAsView("add")

@student_blueprint.route('/student/update', methods=['GET','POST'])
def update_student():
    student_id = request.args.get('student_id', None)
    if student_id is not None:
        data = {
            "student_id": student_id
        }
        return StudentView.renderCreateFormAsView("edit", **data)
    else:
        return StudentView.setPayloadToJSON(404)

@student_blueprint.route('/api/student/create', methods=['POST'])
def api_create_student():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':    
        request_body = request.get_json()
        if request_body:
            student_id = str(request_body['student_id'])
            firstname = str(request_body['firstname'])
            lastname = str(request_body['lastname'])
            course = str(request_body['course'])
            year = str(request_body['year'])
            gender = str(request_body['gender'])
            img_url = str(request_body['img_url'])
            model_response = StudentModel.insert(student_id, firstname, lastname, course, year, gender, img_url)
            return StudentView.setPayloadToJSON(201, payload=model_response)
        else:
            return StudentView.setPayloadToJSON(400)
    else:
        return CollegeView.setPayloadToJSON(403)

@student_blueprint.route('/api/student/read/', methods=['GET'])
def api_read_student():
    student_id = request.args.get('student_id', None)
    model_response = StudentModel.read(student_id)
    return StudentView.setPayloadToJSON(201, payload=model_response)

@student_blueprint.route('/api/student/update', methods=['POST'])
def api_update_student():
    request_body = request.get_json()
    if request_body:
        student_id = str(request_body['student_id'])
        new_student_id = str(request_body['new_student_id'])
        new_firstname = str(request_body['new_firstname'])
        new_lastname = str(request_body['new_lastname'])
        new_course = str(request_body['new_course'])
        new_year = str(request_body['new_year'])
        new_gender = str(request_body['new_gender'])
        model_response = StudentModel.update(student_id, new_student_id, new_firstname, new_lastname, new_course, new_year, new_gender)
        return StudentView.setPayloadToJSON(201, payload=model_response)
    else:
        return StudentView.setPayloadToJSON(400)

@student_blueprint.route('/api/student/delete', methods=['POST'])
def api_delete_student():
    request_body = request.get_json()
    if request_body:
        student_id = str(request_body['student_id'])
        model_response = StudentModel.delete(student_id)
        return StudentView.setPayloadToJSON(201, payload=model_response)
    else:
        return StudentView.setPayloadToJSON(400)

@student_blueprint.route('/api/student/list', methods=['GET', 'POST'])
def api_get_students():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'POST':
            request_body = request.get_json()
            if request_body:
                query = str(request_body['query']).strip()
                model_response = StudentModel.list_all(query)
                render_model = model_response['results']
                return StudentView.renderTableAsJSON(render_model)
            else:
                return StudentView.setPayloadToJSON(400)
        else:
            session['lastTab'] = "Student"  # SESSION
            results = StudentModel.count_rows()
            if results['results'] > 0:
                model_response = StudentModel.list_all()
                render_model = model_response['results']
                return StudentView.renderTableAsJSON(render_model)
            else:
                return StudentView.renderNoDataAsJSON()
    else:
        return StudentView.setPayloadToJSON(403)


@student_blueprint.route('/api/student/image_upload', methods=['POST'])
def api_upload_students():
    request_file = request.files
    request_body = request.form
    if request_body:
        student_id = str(request_body['student_id'])
        if 'image' in request_file:
            image = request_file['image']
            cloudResponse = CloudService.upload(image, student_id, "student")
            results = cloudResponse["results"]
            return StudentView.setPayloadToJSON(201, payload=results)
        else:
            return 'No image provided', 400
    else:
        return StudentView.setPayloadToJSON(400)


@student_blueprint.route('/api/student/image_destroy', methods=['POST'])
def api_image_destroy_students():
    request_body = request.json
    if request_body:
        student_id = str(request_body['student_id'])
        cloudResponse = CloudService.delete(student_id, "student")
        results = cloudResponse["results"]
        return StudentView.setPayloadToJSON(201, payload=results)
    else:
        return StudentView.setPayloadToJSON(400)
