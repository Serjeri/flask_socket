import random
from flask_socketio import SocketIO, emit
from flask import Flask


app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('message')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    while True:
        try:
            emit('message', {'goodbye': random.random()})                        
            socketio.sleep(5)
        except:
            pass