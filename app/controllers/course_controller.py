from flask import Blueprint, request
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
    if code is not None:
        data = {
            "code": code
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
            img_url = str(request_body['img_url'])
            model_response = CourseModel.insert(code, name, college, img_url)
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
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'POST':
            request_body = request.get_json()
            if request_body:
                query = str(request_body['query']).strip()
                model_response = CourseModel.list_all(query)
                render_model = model_response['results']
                return CourseView.renderTableAsJSON(render_model)
            else:
                return CourseView.setPayloadToJSON(400)
        else:
            results = CourseModel.count_rows()
            if results['results'] > 0:
                model_response = CourseModel.list_all()
                render_model = model_response['results']
                return CourseView.renderTableAsJSON(render_model)
            else:
                return CourseView.renderNoDataAsJSON()
    else:
        return CourseView.setPayloadToJSON(403)


@course_blueprint.route('/api/course/upload', methods=['POST'])
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
