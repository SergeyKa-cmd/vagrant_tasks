## How to run:
1. Clone this repo
2. Prepare python virtual environment (e.g. using ```virtualenv```) and docker-engine need to be installed
3. Install flask with command: ```pip3 install flask-restful```
4. Run: ```python3 storage_api.py```
5. Open web browser to http://localhost:5000
6. For using dockerized application need to build it with: ```docker build -t flask-api .``` in current directory with Dockerfile
7. Run container ```docker run -p 5000:5000 flask-api:latest```
8. Open web browser to http://localhost:5000