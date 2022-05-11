import tempfile
import json
import argparse
import os

file_path = os.path.join(tempfile.gettempdir(), 'storage.data')

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

def main():
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
if __name__ == "__main__":
  main();