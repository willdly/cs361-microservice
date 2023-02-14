import zmq
import requests

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("Waiting to request...")

while True:
    socket.recv()
    print('Fetching a random word...\n')
    url = "https://wordsapiv1.p.rapidapi.com/words/"

    querystring = {"random": "true"}

    headers = {
        "X-RapidAPI-Key": "<apikeyhere>",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.json()
    parse_word = result["word"]
    print(f'Random word is {parse_word}.')
    socket.send_string(parse_word)
    print('Random word sent to client...\n')
