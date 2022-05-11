import flask
import tempfile
import json
import argparse
import os

app = flask.Flask(__name__)
#api = Api(app)
file_path = os.path.join(tempfile.gettempdir(), 'storage.data')

DESCRIPTION = """
Прототип API хранилища ключ-значение

Получить все данные хранилища WEB:
http://{HOST_IP:PORT}/api/v1/storage/json/all

Получить все данные хранилища CURL:
curl -i X GET http://{HOST_IP:PORT}/api/v1/storage/json/all

Получить данные хранилища по ключу WEB:
http://{HOST_IP:PORT}/api/v1/storage/json/read?key=test

Получить данные хранилища по ключу CURL:
curl -i -GET http://{HOST_IP:PORT}/api/v1/storage/json/read?key=test

Добавить данные в хранилище хранилища WEB:
curl -i -H "Content-Type: application/json" -X POST -d '{"test3": "value4"}' http://{HOST_IP:PORT}/api/v1/storage/json/write
"""

##Pull data to storage.data file
def pull_data(key, value):
    data = push_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    #Open file to write
    with open(file_path, 'w') as f:
        f.write(json.dumps(data))

##Push data from storage.data file
def push_data():
    if not os.path.exists(file_path):
        return {}
    #Read file and return values
    with open(file_path, 'r') as r:
        data = r.read()
        if data:
            return json.loads(data)
        return {}
##Get list of values
def get_data_list(key):
    data = push_data()
    #Call method get from dict
    return data.get(key)

def validate():
    ##Section for parsing arguments from program
    parser = argparse.ArgumentParser()
    #define command line options arguemnts 
    parser.add_argument("--key", "-k", help="Get or Add key argument")
    parser.add_argument("--value", "-v", help="Get or Add value argument")
    #read arguments at command line
    args = parser.parse_args()
    #Check for exceptions and errors from try: to except block
    try:
        #check for arguments
        if args.key and args.value:
            pull_data(args.key, args.value)
        elif args.key:
            print(get_data_list(args.key))
        else:
            print('List of commands is: --key, --value')
    except:
        print(None)
    #print(args)

##Get all API options
@app.route('/', methods=['GET'])
def root_handler():
    return flask.render_template("root.html", DESCRIPTION=DESCRIPTION)
##Get All key-values
@app.route('/api/v1/storage/json/all', methods=['GET'])
def all_get_handler():
    return flask.jsonify(push_data())
##Get value via key
@app.route('/api/v1/storage/json/read', methods=['GET'])
def key_get_handler():
    key = flask.request.args['key']
    return flask.jsonify({'result': get_data_list(key)})
##POST key-value
@app.route('/api/v1/storage/json/write', methods=['POST'])
def post_handler():
    #Check command condition
    if not flask.request.json:
        flask.abort(400)
    #Serialization JSON to dict
    parse_json = flask.request.json
    data_dict = json.dumps(parse_json)
    #Parse key-values to arguments
    for key, value in parse_json.items():
        #Pass arguments to function
        pull_data(key, value)
    return (f'Success add data {data_dict}.')

if __name__ == "__main__":
  #app.debug = True
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
