import zmq


def fetch_randword():
    context = zmq.Context()

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    socket.send(b'Fetch random word')

    message = socket.recv()
    decoded_message = message.decode()
    print(f'{decoded_message}\n')


while True:
    choice = input('Would you like to learn a new word? (Y/N): ')
    if choice == "N":
        break
    elif choice != "Y":
        print('\n Invalid response, please try again.')
        continue
    else:
        fetch_randword()
