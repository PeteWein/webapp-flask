FROM python:alpine3.7
ADD . /webapp-flask
WORKDIR /webapp-flask
COPY . /webapp-flask
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./webapp-flask/app.py