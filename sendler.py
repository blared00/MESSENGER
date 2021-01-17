import requests

name = input('Vvedite imya')
while True:
    text = input('Vvedite text')
    response = requests.post(
        'http://127.0.0.1:5000/send',
        json={'text': text,
                'name': name}
    )


