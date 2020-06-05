FROM python:alpine3.7
COPY . /webapp-flask
WORKDIR /webapp-flask
RUN pip install -r webapp-flask/requirements.txt
EXPOSE 5000
ENV FLASK_APP webapp-flask
CMD flask run