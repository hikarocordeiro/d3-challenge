from flask import (
    Blueprint, render_template
)

from werkzeug.exceptions import abort

bp = Blueprint('covid19', __name__)

@bp.route('/')
def index():
    return render_template('covid19/index.html')