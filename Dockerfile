FROM python:alpine3.7
ADD . /application
WORKDIR /application
COPY . /application
RUN pip install -r requirements.txt
EXPOSE 5000
CMD flask run