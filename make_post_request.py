import json
import time
import requests


if __name__ == '__main__':

	URL = 'http://localhost:5001/handle_post'

	while True:
		time.sleep(2)
		post_data = {'login': 'login', 'password': 'password'}
		r = requests.post(URL, data=json.dumps(post_data))
		print(f'STATUS: {r.status_code}, BODY: {r.text}')
