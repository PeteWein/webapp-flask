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
WORKDIR /webapp-flask-ui
#ENV PATH /application/node_modules/.bin:$PATH
COPY package.json ./
COPY package-lock.json ./
EXPOSE 3000
RUN npm install
CMD npm run