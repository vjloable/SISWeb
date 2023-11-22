import os
from flask import render_template, Blueprint, request
from app.services.cloud_service import CloudService

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
@index_blueprint.route('/index')
def index():
    return render_template('index.html')

@index_blueprint.route('/test')
def test():
    return render_template('test.html')

@index_blueprint.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        image = request.files['image']
        url = CloudService.upload(image,"test","college")
        return url
    else:
        return 'No image provided', 400
