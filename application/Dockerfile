# flask backend
FROM python:alpine3.7 AS flask_backend
ADD . /application
WORKDIR /application
COPY . /application
RUN pip install -r requirements.txt
ENV FLASK_ENV "development"
EXPOSE 5000
CMD flask run --host=0.0.0.0
