# Developer Utility Scripts

This is a quick start guide to get a developer environment rolling.

**Requirements**

You will need to have python 3.7.x installed for this to work correctly. Beyond that, all of the methods attempt to isolate the dependencies as much as possible (virtual envrionment, container).

**Methods**

There are 3 supported methods to get the webapp online locally: 

* Docker -- this is OS agnostic but requires downloading Docker
* Powershell -- Windows specific environment
* Shell -- linux/MacOS specific environment

This will review all 3 methods.

1. Docker
   - Ensure you have docker installed. More information can be found here: https://docs.docker.com/get-docker/
   - From the project root (where the Dockerfile is located), Run the docker build command
     - this will ideally be removed and you will only have to pull it down in the future 
     -  e.g. `docker pull pwein/flask-backend` or `docker pull pwein/react-frontend`
        - _Note:_ if you want a specific version, you can always add a `:` and the name of the tag, e.g. `docker pull pwein/flask-backend:0.0.5` 
   - After building the image, launch the container with the app
     - e.g. `docker run --publish 5000:5000 -d --name test pwein/flask-backend`  
        - _Note:_ publish denotes which port will be exposed, d runs in headless, name is the container name, and the last line is whatever name and tag of the image you chose. In addition, you can also add a semicolon and tag for a different version (`--name test pwein/flask-backend:0.0.5`) 
   - Assuming everything worked, you are free to visit `http://
   - **NOTE:** We also have a `docker-compose` initialize setup, in case you a) want to turn those docker commands into 1 and b) if you want to see the server with an nginx proxy.
      - In the root project directory: `docker-compose up` 
      - With this setup, you should just be able to go to `http://0.0.0.0` or `http://localhost`
localhost:5000` and confirm.   
2. Powershell
   - Navigate to the `utils` directory and locate the `run_app.ps1` script.
   - From the root of the project, run the following command: `.\utils\run_app.ps1`
     - This will set the appropriate variables, create the virtual envrionment, download dependencies, and launch the webapp.
   - Assuming everything has worked, you can navigate to `http://localhost:5000` and confirm. 
3. Bash
   - Navigate to the `utils` directory and locate the `run_app.sh` script.
   - From the root of the project, run the following command: `./utils/run_app.sh`
     - This will set the appropriate variables, create the virtual envrionment, download dependencies, and launch the webapp.
   - Assuming everything has worked, you can navigate to `http://localhost:5000` and confirm. 
