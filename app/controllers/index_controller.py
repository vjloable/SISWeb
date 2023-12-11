import os
from flask import render_template, Blueprint, request, session, render_template_string, redirect
from flask_session import Session
from app.services.cloud_service import CloudService

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
@index_blueprint.route('/index')
def index():
    if not session.get('lastTab'):
        session['lastTab'] = "College"
    return render_template('index.html')

@index_blueprint.route('/last_tab')
def last_tab():
    return session.get('lastTab')


@index_blueprint.route('/viewmode', methods=['POST'])
def toggle_viewmode():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.method == 'POST':
            request_body = request.get_json()
            if request_body:
                mode = str(request_body['viewmode']).strip()
                session["viewmode"] = mode
                return redirect('/')
            else:
                return f'Invalid request data', 400
        else:
            return f'Forbidden', 403
    else:
        return 'Forbidden', 403


# @index_blueprint.route('/upload', methods=['POST'])
# def upload():
#     if 'image' in request.files:
#         image = request.files['image']
#         url = CloudService.upload(image, "test", "college")
#         return url
#     else:
#         return 'No image provided', 400

# @index_blueprint.route('/test')
# def test():
#     return render_template_string("{{ session['lastTab'] }}")

