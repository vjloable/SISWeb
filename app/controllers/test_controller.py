from flask import render_template, Blueprint

test_blueprint = Blueprint('test', __name__)

@test_blueprint.route('/')
@test_blueprint.route('/index')
def index():
    return render_template('test.html')