FROM jazzdd/alpine-flask:python3

ENV USER_ID=1000
ENV GROUP_ID=1000
ENV USER_NAME=python-flask
ENV GROUP_NAME=python-flask

RUN addgroup -g $GROUP_ID $GROUP_NAME && \
    adduser --shell /sbin/nologin --disabled-password \
    --no-create-home --uid $USER_ID --ingroup $GROUP_NAME $USER_NAME

RUN pip3 install flask-socketio==5.2.0
WORKDIR /app
COPY ./app ./
RUN chown -R python-flask:python-flask /app

USER $USER_NAME
#EXPOSE 5000
ENTRYPOINT ["python3", "web_service.py"]
