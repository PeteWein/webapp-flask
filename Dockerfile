FROM python:alpine3.7
COPY . /webapp-flask
WORKDIR /webapp-flask
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python app.py -h 0.0.0.0