[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

# OPA Auth
This app is responsible to return an user access given a username and role. The usernames and roles are saved in an [OPA](https://www.openpolicyagent.org/) (open policy agent) service.

## How to run

The application can be run with Docker compose or in a Kubernetes cluster (for example, minikube). But before that, you have to create a `.env` file with some environment variables. You can check the template example on the `.env_template` file.

### Docker compose

With docker compose, you just need to run the following command:
```bash
docker-compose up --build
```

PS: Make sure you have Docker installed and running.

### Kubernetes cluster

With a kubernetes cluster, there is a file `k8s/setup.sh` with some commands to setup the app and OPA in the cluster. You can just run the following two commands:
```bash
cd k8s
setup.sh
```

PS: Make sure you have a kubernetes cluster up and running (you can use minikube as well).

## Endpoints

### User access
**You send:**  The username and role

**You get:** The info about the user access

**Request Example:**
```json
POST api/user-access/

{
    "username": "joe",
    "role": "admin"
}
```
**Successful Response Example:**
```json
Status: 200 OK
{
    "hasAccess": true
}
```
**Failed Response Example:**
```json
Status: 422 Unprocessable Entity
{
    "detail": [
        {
            "loc": [
                "body",
                "username"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
``` 
