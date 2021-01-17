import requests
import datetime as d
import time


def print_message(message):
    time_message = d.datetime.fromtimestamp(float(message['time']))
    print(time_message, 'ot', message['name'])
    print(message['text'])
    print()


def print_messages(db):
    for message in db:
        print_message(message)


after = 0

while True:
    response = requests.get(
        'http://127.0.0.1:5000/messenger',
        params={'after': after}

    )

    messages = response.json()['messages']
    for message in messages:
        print_message(message)
        after = message['time']

    time.sleep(1)
