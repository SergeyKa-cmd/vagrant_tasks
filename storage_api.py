#from crypt import methods
import flask
import tempfile
import json
import argparse
import os

from flask_restful import Resource
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
http://{HOST_IP:PORT}/api/v1/storage/json?key=test

Получить данные хранилища по ключу CURL:
curl -i -GET http://{HOST_IP:PORT}/api/v1/storage/json/read?key=test

Добавить данные в хранилище хранилища WEB:
curl -i -H "Content-Type: application/json" -X POST -d '{"test3": "value4"}' http://{HOST_IP:PORT}/api/v1/storage/json/write
"""
class API(Resource):
    ##Pull data to storage.data file
    def pull_data(self, key, value):
        data = self.push_data()
        if key in data:
            data[key].append(value)
        else:
            data[key] = [value]
        #Open file to write
        with open(file_path, 'w') as f:
            f.write(json.dumps(data))

    ##Push data from storage.data file
    def push_data(self):
        if not os.path.exists(file_path):
            return {}
        #Read file and return values
        with open(file_path, 'r') as r:
            data = r.read()
            if data:
                return json.loads(data), 200
            return {}, 404
    ##Get list of values
    def get_data_list(self, key):
        data = self.push_data()
        #Call method get from dict
        return data.get(key), 200

    def validate(self):
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
                self.pull_data(args.key, args.value)
            elif args.key:
                print(self.get_data_list(args.key))
            else:
                print('List of commands is: --key, --value')
        except:
            print(None)
        #print(args)

@app.route('/', methods=['GET'])
def root_handler():
    return flask.render_template("root.html", DESCRIPTION=DESCRIPTION)

@app.route('/get', methods=['GET'])
def get_handler():
    return(API.get_data_list(API.validate))

@app.route('/post', methods=['POST'])
def post_handler():    
    return(API.pull_data(API.args.key, API.args.value))

if __name__ == "__main__":
  app.debug = True
  app.run()
