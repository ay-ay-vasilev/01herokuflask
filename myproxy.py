from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    msg = ""
    if request.args.get('url'):
        try:
            r = requests.get(request.args['url'])
            if r.status_code == 200:
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
