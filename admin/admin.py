from flask import (
  Blueprint, redirect, render_template, request, url_for
)

bp = Blueprint('admin', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
  # query database and put data into render template

  # display admin
  return render_template('admin/index.html')