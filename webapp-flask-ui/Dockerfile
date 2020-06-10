# react front end
FROM node:12.18.0-slim AS react_frontend
ADD . /ui
WORKDIR /ui
COPY . /ui
ENV PATH /node_modules/.bin:$PATH
COPY /package.json ./
COPY package-lock.json ./
EXPOSE 3000
RUN npm install
CMD npm start
