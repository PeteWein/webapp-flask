# webapp-flask
A learning repo designed to create a webapp.

**Docker**

Currently, the docker images are hosted publicly here:

Frontend:
`https://hub.docker.com/r/pwein/react-frontend`

Backend:
`https://hub.docker.com/r/pwein/flask-backend`

If you are interested in looking at the versions currently available -- the tag associated to the image should reflect the tagged source code in the main github repository. 

**Building**

Please feel free to go into the `utils` directory for building locally. Generally speaking, the easiest way is with the docker-compose.yml file at the project root. To run this, you must first have docker installed. 

From there, simply run:

`docker-compose up` 

from the the project root. This will launch both the front-end and back-end, as well as an nginx proxy.

**Source**

Tutorial for buidling flask found here:
https://hackersandslackers.com/your-first-flask-application