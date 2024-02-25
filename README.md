# fastapi-activities
## Description
FastAPI web service that performs the following functionality:
* The PostgreSQL image is deployed using docker-compose. Data safety is ensured during container restart (volumes are used to store DBMS files on the host machine.)
* End-point /get_activity/ - accepts POST requests with {"participants": integer} as input
* After receiving the request, the service, in turn, requests from the public API: https://www.boredapi.com/api/activity?participants=1 the number of participants specified in the received request.
* The received responses are saved in the database (id, activity name, activity type, activity creation date). If there is the same activity in the database, additional requests are made to the public API until a unique activity is received.
* The response to the request is the previous saved activity. If it is missing, it is an empty object.

## Technologies
* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Docker (docker-compose)

## Installation and usage
Clone the repository
```
git clone git@github.com:fooniquler/fastapi-activities.git
```
Go to the fastapi-activities directory
```
cd fastapi-activities
```
Run docker-compose
```
docker-compose up --build
```
