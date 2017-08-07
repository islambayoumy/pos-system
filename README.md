# POS System
Simple POS system API developed using python [Django](https://www.djangoproject.com) framework.


### Application features
* RESTful api based
* Docker image with all required dependencies  
* API documented using [Swagger](https://app.swaggerhub.com/)

## Getting Started

### Prerequisites
Following steps assume that you have installed  
1. [Docker](https://www.docker.com)  
2. [Docker Compose](https://docs.docker.com/compose)  

### Instruction for running the project

- Open terminal and change directory to whatever you want  
~ choosen driver must by shared with docker 
- Clone the project  
`git clone https://github.com/islambayoumy/pos-system`
- change directory to project folder  
`cd pos-system`
- Run the following command for building and start docker image & containers and run the project  
`docker-compose up --build`
- Now you can browse the application through http://127.0.0.1:8000

##### ~ Project isn't ready for production environment yet

#### Using the application
1. A default superuser were created using [Django Finalware](https://github.com/un33k/django-finalware)
~ for development mode only
2. Go to http://127.0.0.1:8000/api/items , there is no records in the database yet 
3. Check API documentation [here](https://app.swaggerhub.com/apis/islambayoumy/pos_system/1.0.0)

## Implementation
 - python3 & django for back-end restful api
 - postgres for db
 
