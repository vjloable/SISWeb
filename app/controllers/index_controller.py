from flask import render_template, Blueprint

index_blueprint = Blueprint('index', __name__)

@test_blueprint.route('/')
@test_blueprint.route('/index')
def index():
    return render_template('index.html')