import math

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
    img_url = request.args.get('img_url', "")
    if student_id is not None:
        data = {
            "student_id": student_id,
            "img_url": img_url
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
            model_response = StudentModel.insert(student_id, firstname, lastname, course, year, gender)
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
    query = str(request.args.get('query', "")).strip()
    page = int(request.args.get('page', 1))
    if page > 0:
        session['lastTab'] = "Student"  # SESSION
        result_count = StudentModel.count_rows()
        if result_count['results'] > 0:
            page = 1 if page < 1 else page
            page_size = 11
            page_number = page - 1
            offset = page_number * page_size
            model_response = StudentModel.get_list(offset, query)
            query_count = StudentModel.count_rows(query)
            max_page = math.ceil(query_count['results'] / 11)
            max_page = 1 if max_page < 1 else max_page
            prev_page = page if (page-1) < 1 else page-1
            next_page = max_page if (page+1) > max_page else page+1
            render_model = {
                "results": model_response['results'],
                "current_page": page,
                "max_page": max_page,
                "prev_page": prev_page,
                "next_page": next_page,
            }
            return StudentView.renderTableAsJSON(render_model)
        else:
            return StudentView.renderNoDataAsJSON()
    else:
        model_response = StudentModel.get_list(-1, query)
        return StudentView.setPayloadToJSON(201, payload=model_response)


@student_blueprint.route('/api/student/image_url_set', methods=['POST'])
def api_image_url_students():
    request_body = request.get_json()
    if request_body:
        student_id = str(request_body['student_id'])
        url = str(request_body['url'])
        model_response = StudentModel.upload_image_url(student_id, url)
        return StudentView.setPayloadToJSON(201, payload=model_response)
    else:
        return StudentView.setPayloadToJSON(400)

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


@student_blueprint.route('/api/student/image_rename', methods=['POST'])
def api_image_rename_students():
    request_body = request.json
    if request_body:
        student_id = str(request_body['student_id'])
        new_student_id = str(request_body['new_student_id'])
        cloudResponse = CloudService.rename(student_id, new_student_id, "student")
        results = cloudResponse["results"]
        return StudentView.setPayloadToJSON(201, payload=results)
    else:
        return StudentView.setPayloadToJSON(400)
