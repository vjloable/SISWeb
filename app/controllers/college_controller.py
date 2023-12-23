import math

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
    img_url = request.args.get('img_url', "")
    if code is not None:
        data = {
            "code": code,
            "img_url": img_url
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
            model_response = CollegeModel.insert(code, name)
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
    query = str(request.args.get('query', "")).strip()
    page = int(request.args.get('page', 1))
    if page > 0:
        session['lastTab'] = "College"  # SESSION
        result_count = CollegeModel.count_rows()
        if result_count['results'] > 0:
            page = 1 if page < 1 else page
            page_size = 11
            page_number = page - 1
            offset = page_number * page_size
            model_response = CollegeModel.get_list(offset, query)
            query_count = CollegeModel.count_rows(query)
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
            return CollegeView.renderTableAsJSON(render_model)
        else:
            return CollegeView.renderNoDataAsJSON()
    else:
        model_response = CollegeModel.get_list(-1, query)
        return CollegeView.setPayloadToJSON(201, payload=model_response)
        

@college_blueprint.route('/api/college/image_url_set', methods=['POST'])
def api_image_url_colleges():
    request_body = request.get_json()
    if request_body:
        code = str(request_body['code'])
        url = str(request_body['url'])
        model_response = CollegeModel.upload_image_url(code, url)
        return CollegeView.setPayloadToJSON(201, payload=model_response)
    else:
        return CollegeView.setPayloadToJSON(400)

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

@college_blueprint.route('/api/college/image_destroy', methods=['POST'])
def api_image_destroy_colleges():
    request_body = request.json
    if request_body:
        code = str(request_body['code'])
        cloudResponse = CloudService.delete(code, "college")
        results = cloudResponse["results"]
        return CollegeView.setPayloadToJSON(201, payload=results)
    else:
        return CollegeView.setPayloadToJSON(400)

@college_blueprint.route('/api/college/image_rename', methods=['POST'])
def api_image_rename_colleges():
    request_body = request.json
    if request_body:
        code = str(request_body['code'])
        new_code = str(request_body['new_code'])
        cloudResponse = CloudService.rename(code, new_code, "college")
        results = cloudResponse["results"]
        return CollegeView.setPayloadToJSON(201, payload=results)
    else:
        return CollegeView.setPayloadToJSON(400)
