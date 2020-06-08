# flask backend
FROM python:alpine3.7
ADD . /application
WORKDIR /application
COPY . /application
RUN pip install -r requirements.txt
ENV FLASK_ENV "development"
EXPOSE 5000
CMD flask run --host=0.0.0.0

# react front end
FROM node:0.12.18
WORKDIR /application/webapp-flask-ui
RUN echo $(ls -1 /tmp/dir)
#ENV PATH /application/node_modules/.bin:$PATH
#COPY /application/webapp-flask-ui/package.json ./
#COPY /application/webapp-flask-ui/package-lock.json ./
EXPOSE 3000
RUN npm install
CMD npm run