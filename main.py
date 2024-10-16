# No seu main.py
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET"] = "KEY"
app.config["DEBUG"] = True
socketio = SocketIO(app, cors_allowed_origins="*")  # Permitir todas as origens

@socketio.on("message")
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5001, allow_unsafe_werkzeug=True)
