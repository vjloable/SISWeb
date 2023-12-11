from flask import Blueprint, request, session
from flask_session import Session
from app.models.college_model import CollegeModel
from app.views.college_view import CollegeView
from app.services.cloud_service import CloudService

college_blueprint = Blueprint('college', __name__)

@college_blueprint.route('/college/create', methods=['GET'])
def create_college():
    return CollegeView.renderCreateFormAsView("add")

@college_blueprint.route('/college/update', methods=['GET'])
def update_college():
    code = request.args.get('code', None)
    if code is not None:
        data = {
            "code": code
        }
        return CollegeView.renderCreateFormAsView("edit", **data)
    else:
        return CollegeView.setPayloadToJSON(404)

@college_blueprint.route('/api/college/create', methods=['POST'])
def api_create_college():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        request_body = request.get_json()
        if request_body:
            code = str(request_body['code']) 
            name = str(request_body['name'])
            img_url = str(request_body['img_url'])
            model_response = CollegeModel.insert(code, name, img_url)
            return CollegeView.setPayloadToJSON(201, payload=model_response)
        else:
            return CollegeView.setPayloadToJSON(400)
    else:
        return CollegeView.setPayloadToJSON(403)
    
@college_blueprint.route('/api/college/read', methods=['GET'])
def api_read_college():
    code = request.args.get('code', None)
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
        return CollegeView.setPayloadToJSON(201, payload=model_response)
    else:
        return CollegeView.setPayloadToJSON(400)

@college_blueprint.route('/api/college/list', methods=['GET', 'POST'])
def api_get_colleges():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'POST':
            request_body = request.get_json()
            if request_body:
                query = str(request_body['query']).strip()
                model_response = CollegeModel.list_all(query)
                render_model = model_response['results']
                return CollegeView.renderTableAsJSON(render_model)
            else:
                return CollegeView.setPayloadToJSON(400)
        else:
            session['lastTab'] = "College" #SESSION
            results = CollegeModel.count_rows()
            if results['results'] > 0:
                model_response = CollegeModel.list_all()
                render_model = model_response['results']
                return CollegeView.renderTableAsJSON(render_model)
            else:
                return CollegeView.renderNoDataAsJSON()
    else:
        return CollegeView.setPayloadToJSON(403)

@college_blueprint.route('/api/college/image_upload', methods=['POST'])
def api_image_upload_colleges():
    request_file = request.files
    request_body = request.form
    if request_body:
        code = str(request_body['code'])
        if 'image' in request_file:
            image = request_file['image']
            cloudResponse = CloudService.upload(image, code, "college")
            results = cloudResponse["results"]
            return CollegeView.setPayloadToJSON(201, payload=results)
        else:
            return 'No image provided', 400
    else:
        return CollegeView.setPayloadToJSON(400)

# @college_blueprint.route('/api/college/image_destroy', methods=['POST'])
# def api_image_destroy_colleges():
#     request_body = request.form
#     if request_body:
#         code = str(request_body['code'])
#         cloudResponse = CloudService.delete(code, "college")
#         results = cloudResponse["results"]
#         return CollegeView.setPayloadToJSON(201, payload=results)
#     else:
#         return CollegeView.setPayloadToJSON(400)
