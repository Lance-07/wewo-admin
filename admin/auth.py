from flask import (
  Blueprint, request, render_template, flash, redirect, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST', 'GET'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    errors = None

    print(f'username: {username} & password: {password}')

    return redirect( url_for('index') )


  return render_template('auth/register.html')


@bp.route('/login', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    errors = None

    print(f'username: {username} & password: {password}')
    
    return redirect( url_for('index') )

  return render_template('auth/login.html')
