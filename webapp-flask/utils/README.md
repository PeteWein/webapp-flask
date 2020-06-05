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
     -  e.g. `docker build --tag flask-webapp:test . ` 
        - _Note:_ the name of the app and tag can be whatever you want, this is just the easiest for documentation.
   - After building the image, launch the container with the app
     - e.g. `docker run --publish 5000:5000 -d --name test flask-webapp:test`  
        - _Note:_ publish denotes which port will be exposed, d runs in headless, name is the contianer name, and the last line is whatever name and tag of the image you chose.
   - Assuming everything worked, you are free to visit `http://localhost:5000` and confirm.   
2. Powershell
   - Navigate to the `utils` directory and locate the `run_app.ps1` script.
   - From the root of the project, run the following command: `.\webapp-flask\utils\run_app.ps1`
     - This will set the appropriate variables, create the virtual envrionment, download dependencies, and launch the webapp.
   - Assuming everything has worked, you can navigate to `http://localhost:5000` and confirm. 
3. Bash
   - Navigate to the `utils` directory and locate the `run_app.sh` script.
   - From the root of the project, run the following command: `./webapp-flask/utils/run_app.sh`
     - This will set the appropriate variables, create the virtual envrionment, download dependencies, and launch the webapp.
   - Assuming everything has worked, you can navigate to `http://localhost:5000` and confirm. 
