from flask_socketio import SocketIO, send
from website import create_app

app = create_app()
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(message):
    print("Recieved message: " + message)
    if message != "User connected!":
        send(message, broadcast=True)
    


if __name__ == "__main__":
    # socketio.run(app, debug=True, host="192.168.0.102", port=5053)
    socketio.run(app, debug=True)
