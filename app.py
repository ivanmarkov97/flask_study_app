from flask import Flask, session, redirect, url_for, render_template

from db_manager.db_manager import DBManager
from utils import config_from_file

app = Flask(__name__)
app.secret_key = 'my secret password'

db_config = config_from_file('DB_CONFIG.yml')
app.config['db_config'] = db_config

from blueprints.auth import auth


app.register_blueprint(auth, prefix='/')

# @app.route('/handle_post', methods=['POST', 'GET'])
# def handler():
# 	data = request.data.decode('utf-8') # делаем строку из байтов согласно кодировке
# 	json_data = json.loads(data) # делаем json из стркои
# 	return json_data


@app.route('/')
def index():
	if 'login' not in session:
		return redirect(url_for('auth_bp.login'))
	else:
		return render_template('index.html')


with DBManager(db_config) as cursor:
	cursor.execute("select version()")
	sql_result = cursor.fetchall()
	print(sql_result)


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5001)
