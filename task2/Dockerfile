FROM python:3-alpine
MAINTAINER Sergey Karakulanov <serdj-999@yandex.ru>
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app
EXPOSE 5000
CMD ["python", "./storage_api.py"]