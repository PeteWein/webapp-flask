FROM python:alpine3.7
WORKDIR /webapp-flask
COPY . /webapp-flask
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./webapp-flask/app.py -h 0.0.0.0