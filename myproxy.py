from flask import Flask
from flask import request
import requests

import mysql.connector
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
	msg = ""
	if request.args.get('url'):
		try:
			r = requests.get(request.args['url'])
			if r.status_code == 200:
				ip_client = request.remote_addr
				J = json.load(open('/config/config.json'))
				ip = J['ip']
				now = datetime.now()
				cnx = mysql.connector.connect(user='myproxy', database='myproxy', host=ip, password='1234zxcv')
				cursor = cnx.cursor()
				cursor.execute(
					"INSERT INTO myproxy.log VALUES(%s, %s, %s)",
					(now, ip_client, request.args['url'])
				)
				cnx.commit()
				return  r.content

		except:
			msg = f"Не удалось загрузить {request.args.get('url')}"
	return  '<h1>' + msg + '''</h1>
			Hey IVT-17!<br/>
			<form method="get">
				<input type="text" name="url">
				<input type="submit">
			</form>
			'''
	


if __name__ == '__main__':
	app.run()
