# DevOps Web Application
A learning repo designed to create an end-to-end devops pipeline without incurring any costs for deployment/hosting. Below are the components current in use:

- Github: Source control management, webhooks to push to other components
- Docker Hub: Host images built for the front end and back end
- Heroku: Final application deployment

**Workflow Description**

Generally speaking, this is how the workflow is designed to operate and speed up the CICD pipeline deployment process.

1. Developer follows standard update pattern
    - clone repo, create branch, make changes, test changes locally, push changes, create pull request
2. On pull request creation, CODEOWNERS automatically assigned as reviewers
    -  automatic testing is then run using github workflows. Currently there is one sample test that runs
    -  automatic docker build is run on front end and back end to confirm they still build correctly
3. Assuming all tests pass and reviewers sign off, code merged into master and branch is deleted
4. Upon merging into master, webhook pushes new update to both Docker Hub and Heroku
    - *Note*: Ideally it would first build in docker hub, and then the application would run docker and pull the new tagged images. Heroku has a bit of trouble with this and would require also building images in their container registry, which adds additional complexity
5. Docker hub will update the the image appropriate (latest for a master branch update, release-{{ release tag }} for releases)
6. Heroku will build the new code and deploy to the server.


**Heroku**

The final application can be found here:

https://pwein-webapp-sample.herokuapp.com/home

**Docker**

Currently, the docker images are hosted publicly here:

Frontend:
`https://hub.docker.com/r/pwein/react-frontend`

Backend:
`https://hub.docker.com/r/pwein/flask-backend`

If you are interested in looking at the versions currently available -- the tag associated to the image should reflect the tagged source code in the main github repository. 

**Local Deployment**

Please feel free to go into the `utils` directory for information on local deployments, as well as additional options. The easiest way/recommended route is with the docker-compose.yml file at the project root. To run this, you must first have docker installed. 

From there, simply run:

`docker-compose up` 

from the the project root. This will launch both the front-end and back-end, as well as an nginx proxy.
