# Cool GeoAPP

This is the README for the Cool GeoAPP Challenge for Carto.
In the following section, we will describe the challenge and the solution.

## The challenge

The challenge is to develop an API that allows users to query some data about population of Madrid and some geographical
data.

For resolution of the challenge I've used the following technologies:

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/)
* [Redis](https://redis.io/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)
* [Swagger](https://swagger.io/)

Note that the image of Docker for PostgreSQL is a prebuilt image with PostGIS.

## Project structure

The project structure adopted for the challenge is a kind of hexagonal architecture. With that we can divide the project
into domains and make the project more modular, mainteanable and scalable if you want to add some new features.

The project structure is as follows:

```scala
$ tree -L 5 src
src
├── __init__.py
├── postal_code
│   ├── __init__.py
│   ├── application
│   │   ├── PostalCodeFinder.py
│   │   ├── PostalCodeLister.py
│   │   └── __init__.py
│   ├── domain
│   │   ├── PostalCodeId.py
│   │   ├── PostalCodeRepository.py
│   │   └── __init__.py
│   └── infrastructure
│       ├── PostalCodePostgresRepository.py
│       └── __init__.py
├── shared
│   ├── __init__.py
│   ├── domain
│   │   ├── ValueObject.py
│   │   └── __init__.py
│   └── infrastructure
│       ├── PostgresClient.py
│       ├── RedisClient.py
│       └── __init__.py
└── turnover
    ├── __init__.py
    ├── application
    │   ├── TurnoverByAge.py
    │   ├── TurnoverByDate.py
    │   ├── TurnoverTotal.py
    │   └── __init__.py
    │  
    ├── domain
    │ ├── InvalidDateException.py
    │ ├── TurnoverRepository.py
    │ ├── __init__.py
    │ └── __pycache__
    │     ├── InvalidDateException.cpython-39.pyc
    │     └── TurnoverRepository.cpython-39.pyc
    └── infrastructure
        ├── TurnoverPostgresRepository.py
        └── __init__.py
```

## Execute the challenge

For executing the challenge just run the following command:

    $ make build

This command will generate the Docker containers, populate the DB and start the API service which runs in localhost:8000

Also, if you want to check the API documentation, just go to the following url:

    localhost:8080

## Future development

We can add some new features to the API. For example:

* Modify the API to securize the access to the API via JWT or
  OAuth2
* Add different formats for the postal codes like KML