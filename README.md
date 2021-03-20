<h1 align="center">Welcome to Docker Flask Mongo Crud 👋</h1>
<p>
</p>

> Project based off a recent interview "take home" project.

### [App](localhost:5001/)

## Summary of Reqs
- Generate multiple unique endpoints that can be called simultaneously
- Receive a Restful HTTP POST
- Persist the contents of the POST to a datastore
- Run in a Docker container
- Include a functioning health check
- Include sufficient documentation to enable other developers to support your app

## Reqs Checklist
- [ ] Use a Docker container to host your service.
- [ ] Provide a service endpoint that will generate a unique URI.
- [ ] Allow POST operations to that generated endpoint.
- [ ] Store the contents (BODY) of the POST to a persistent datastore.
- [ ] Include a health check that will monitor your service.
- [ ] Accept GET requests to the service endpoint that will return the body of the most recent POST operation.
- [ ] Include a README that provides instructions on setting up and running your app. Be sure to call out any dependencies as well.

## Assumptions/Local Env Info
- Built on Pop_OS 20.04.
- Will be ran on x86 based system.
    - Will not run on ARM devices.
- Docker version 19.03.8.
- docker-compose version 1.25.0.
- Access to Docker Hub.
- Data does not need persistance.
- Ran on accessible via localhost.
- No conflicting ports.
    - App 5001
- Data being transmitted via request is not sensitive. 
- One record will be created/updated/deleted at a time.

## Dependencies
- docker
- docker-compose
- Containers:
    - mongo
    - python:alpine

## Install

```sh
clone repo/unpack archive
```

## Usage
Within the app directory:
```sh
docker-compose up --build  
```
Clean-Up:
```sh
docker-compose down
```
Additional Image clean-up is required, but requires knowing more about your local dev environment.<br />

## Endpoints/Methods

```sh
# Health Check
Get http://localhost:5001/
# Create User
Post http://localhost:5001/users name:a, lastName:AA
# Report Recent Users
Get http://localhost:5001/users
# Update User Name (Updating lastName not implemented at this time)
Put http://localhost:5002/users/$mongoID
# Delete User
Delete http://localhost:5001/users/$mongoID

```
Body represented as follows:
```sh
{
    "name": "a",
    "lastname": "bb"
}
```
Response represented as follows:
```sh
[
    {
        "_id": "605413d32a15dafa4d0d5eaf",
        "name": "a",
        "lastname": "bb"
    }
]
```

## Maintanence and Troubleshooting
This section describes troubleshooting the app.<br />
It should be a livin document, updated as new things are discovered and fixed.<br />

### Debugging Application
Additional Debugging can be enabled in the `server.py` file.<br />
This is located toward the end of the file under `# Initalize Host, Port, Debugging`.<br />
Switch `debug=False` with `debug=True`.<br />

### Database Connection Issues
Verify that the connection host string under `# Setup MongoDB Connection`<br />
matches the service name assiociated with mongo in the docker-compose.yml.<br />
Additionally, if you need to troubleshoot the database, you can spin up the<br />
stack and expose the ports, i.e.<br />
```sh
ports:
    - "27017:27017"
```
You can then interact with the database.

## Eval Criteria
- [ ] Are all stated requirements met?
- [ ] Does the application successfully build and run?
- [ ] Is the solution well-organized and easy to understand?
- [ ] Are functions and variables clearly named to express their purpose?
- [ ] Were any scope decisions, TODO items, dependencies, and known issues called out in code comments or the README file?

## Author

👤 **Josh Bailey**

* Github: [@binkocd](https://github.com/binkocd)
* LinkedIn: [@joshuarobertbailey](https://linkedin.com/in/joshuarobertbailey)