from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    ip_client = request.environ['REMOTE_ADDR']
    ip_server = request.remote_addr
    return render_template('index.html', ip_address_of_client=ip_client, server_ip=ip_server)
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
