from datetime import datetime
import time
from flask import Flask, request, abort


app = Flask(__name__)
db = [
    {
        'text': 'Hello!',
        'time': '1610913002.8965557',
        'name': 'Michal'
    },
    {
        'text': 'Hello too!',
        'time': '1610913032.8965557',
        'name': 'Tasty'
    }
]


@app.route('/')
def hello():
    return "Hello world!"


@app.route('/status')
def status():
    now = datetime.now()
    return {'messages': db}


@app.route('/messenger')
def get_message():
    try:
        after = float(request.args['after'])
    except ValueError:
        abort(400)
    #format_time = '%H:%M:%S - %d.%m.%Y'
    messages = []
    for message in db:
        if float(message['time']) > after:
            messages.append(message)

    return {'messages': messages[:100]}


@app.route('/send', methods=['POST'])
def send_message():
    if not isinstance(request.json, dict):
        return abort(400)

    name = request.json.get('name')
    text = request.json.get('text')

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if name == '' or text == '':
        return abort(400)

    message = {
        'text': text,
        'time': time.time(),
        'name': name
    }
    db.append(message)
    return {'ok': True}


app.run()
