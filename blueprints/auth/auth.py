from flask import Blueprint, render_template, request, current_app, url_for
from werkzeug.utils import redirect

from sql_data_provider.sql_data_provider import SQLDataProvider
from utils import write_session, clear_session

auth = Blueprint('auth_bp', __name__,
                 template_folder='templates',
                 static_folder='static',
                 static_url_path='/blueprints/auth')


@auth.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['login']
		password = request.form['password']
		users = SQLDataProvider.get_user_by_login_and_password(username, password, current_app.config['db_config'])
		if users is not None:
			if len(users) > 1:
				raise ValueError('More than one USER detected in system')
			user = users[0]
			write_session(user)
			return redirect('/')
	return render_template('auth/login.html')


@auth.route('/logout')
def logout():
	clear_session()
	return redirect(url_for('auth_bp.login'))
