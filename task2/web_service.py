from flask import Flask, render_template, request
import socket

app = Flask(__name__)
@app.route('/greetings')
def greetings():
    ip_client = request.headers.get('X-Forwarded-For')
    ip_server = request.remote_addr
    return render_template('index.html', ip_address_of_client=ip_client, server_ip=ip_server)
if __name__ == "__main__":
  ip_host = socket.gethostbyname(socket.gethostname())
  app.run(host = ip_host, port=5000)
