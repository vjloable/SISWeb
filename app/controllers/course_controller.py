import math

from flask import Blueprint, request, session
from flask_session import Session
from app.models.course_model import CourseModel
from app.views.course_view import CourseView
from app.services.cloud_service import CloudService

course_blueprint = Blueprint('course', __name__)

@course_blueprint.route('/course/create', methods=['GET'])
def create_course():
    return CourseView.renderCreateFormAsView("add")

@course_blueprint.route('/course/update', methods=['GET','POST'])
def update_course():
    code = request.args.get('code', None)
    img_url = request.args.get('img_url', "")
    if code is not None:
        data = {
            "code": code,
            "img_url": img_url
        }
        return CourseView.renderCreateFormAsView("edit", **data)
    else:
        return CourseView.setPayloadToJSON(404)

@course_blueprint.route('/api/course/create', methods=['POST'])
def api_create_course():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        request_body = request.get_json()
        if request_body:
            code = str(request_body['code']) 
            name = str(request_body['name'])
            college = str(request_body['college'])
            model_response = CourseModel.insert(code, name, college)
            return CourseView.setPayloadToJSON(201, payload=model_response)
        else:
            return CourseView.setPayloadToJSON(400)
    else:
        return CourseView.setPayloadToJSON(403)

@course_blueprint.route('/api/course/read', methods=['GET'])
def api_read_course():
    code = request.args.get('code', None)
    model_response = CourseModel.read(code)
    return CourseView.setPayloadToJSON(201, payload=model_response)

@course_blueprint.route('/api/course/update', methods=['POST'])
def api_update_course():
    request_body = request.get_json()
    if request_body:
        code = str(request_body['code']) 
        new_code = str(request_body['new_code'])
        new_name = str(request_body['new_name'])
        new_college = str(request_body['new_college'])
        model_response = CourseModel.update(code, new_code, new_name, new_college)
        return CourseView.setPayloadToJSON(201, payload=model_response)
    else:
        return CourseView.setPayloadToJSON(400)

@course_blueprint.route('/api/course/delete', methods=['POST'])
def api_delete_course():
    request_body = request.get_json()
    if request_body:
        code = str(request_body['code'])
        model_response = CourseModel.delete(code)
        return CourseView.setPayloadToJSON(201, payload=model_response)
    else:
        return CourseView.setPayloadToJSON(400)

@course_blueprint.route('/api/course/list', methods=['GET','POST'])
def api_get_courses():
    query = str(request.args.get('query', "")).strip()
    page = int(request.args.get('page', 1))
    if page > 0:
        session['lastTab'] = "Course"  # SESSION
        result_count = CourseModel.count_rows()
        if result_count['results'] > 0:
            page = 1 if page < 1 else page
            page_size = 11
            page_number = page - 1
            offset = page_number * page_size
            model_response = CourseModel.get_list(offset, query)
            query_count = CourseModel.count_rows(query)
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
            return CourseView.renderTableAsJSON(render_model)
        else:
            return CourseView.renderNoDataAsJSON()
    else:
        model_response = CourseModel.get_list(-1, query)
        return CourseView.setPayloadToJSON(201, payload=model_response)


@course_blueprint.route('/api/course/image_url_set', methods=['POST'])
def api_image_url_courses():
    request_body = request.get_json()
    if request_body:
        code = str(request_body['code'])
        url = str(request_body['url'])
        model_response = CourseModel.upload_image_url(code, url)
        return CourseView.setPayloadToJSON(201, payload=model_response)
    else:
        return CourseView.setPayloadToJSON(400)

@course_blueprint.route('/api/course/image_upload', methods=['POST'])
def api_upload_courses():
    request_file = request.files
    request_body = request.form
    if request_body:
        code = str(request_body['code'])
        if 'image' in request_file:
            image = request_file['image']
            cloudResponse = CloudService.upload(image, code, "course")
            results = cloudResponse["results"]
            return CourseView.setPayloadToJSON(201, payload=results)
        else:
            return 'No image provided', 400
    else:
        return CourseView.setPayloadToJSON(400)


@course_blueprint.route('/api/course/image_destroy', methods=['POST'])
def api_image_destroy_courses():
    request_body = request.json
    if request_body:
        code = str(request_body['code'])
        cloudResponse = CloudService.delete(code, "course")
        results = cloudResponse["results"]
        return CourseView.setPayloadToJSON(201, payload=results)
    else:
        return CourseView.setPayloadToJSON(400)


@course_blueprint.route('/api/course/image_rename', methods=['POST'])
def api_image_rename_courses():
    request_body = request.json
    if request_body:
        code = str(request_body['code'])
        new_code = str(request_body['new_code'])
        cloudResponse = CloudService.rename(code, new_code, "course")
        results = cloudResponse["results"]
        return CourseView.setPayloadToJSON(201, payload=results)
    else:
        return CourseView.setPayloadToJSON(400)
