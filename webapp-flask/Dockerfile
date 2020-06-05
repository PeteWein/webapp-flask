FROM python:alpine3.7
COPY . /website
WORKDIR /website
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./src/app.py