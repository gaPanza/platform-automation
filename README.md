# Platform Automation

## Description

Basic automation of services configured with Docker and Makefile. This repository contains 2 web applications (Auth and Core APIs) and one Python script simulating and processing transactions in the Core API app. Docker compose is used to facilitate container creation and automation of a local development environment.

To help developers work both web apps, this automation uses Traefik (https://github.com/traefik/traefik) in order to route requests to the desired endpoint. In development, developers can use localhost and the appropriate service to work with. (Eg. 0.0.0.0:5000/auth/health | 0.0.0.0:5000/core/health)

In order to create and facilitate configuration management, this repo contains a makefile file as described below in the quickstart section. An environment file can also be set up and the Traefik dashboard should be turned off in the docker-compose.yaml in order to make this better suited for production.

## Architecture Overview

```
+----------------------------------+
|            Merchant              |
+-+--------^------------+--------^-+
  |        |            |        |
 (1)      (2)          (3)      (5)
  |        |            |        |
+-v--------+-+        +-v--------+-+        +-----------------+
|  Auth API  |        |  Core API  |        |  PSP Connector  | 
+------------+        +------+-----+        +---------^-------+
                             |                        |
                            (4)                      (6)
                             |                        |
                      +------v------------------------+-------+
                      |          Redis Message Queue          |
                      +---------------------------------------+
```

There are 3 distinct services:

- [Auth API] - Creates authentication tokens to valid users.
- [Core API] - Processes transaction requests.
- [PSP Connector] - Processes the transactions with a Payment Service Provider (PSP).

## Dependencies

- Docker
- Makefile

## Quickstart

- Every service is containerized and ready to use locally on localhost.

#### With the c= param it's possible to specify the container when running the make commands below
##### Options are auth | core | psp-conn

##### Build Project
```shell
make build
```

##### Run Project
```shell
make up
```

- In order to test services a GET request can be performed. Eg.
```shell
http -v http://0.0.0.0:5000/auth/health
```

##### Response

```http
HTTP/1.1 200 
content-length: 29
content-type: application/json
date: Mon, 12 Sep 2022 12:20:46 GMT
server: hypercorn-h11

{
    "checks": {},
    "status": "pass"
}
```

##### See all application logs
```shell
make logs
```

##### See Auth application logs
```shell
make logs c=auth
```

##### To stop services
```shell
make stop
```

##### To clean the docker environment
```shell
make clean
```



