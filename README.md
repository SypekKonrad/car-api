hosted at: http://3.79.107.161

# Car API Documentation
Welcome to the Car API documentation. This API allows you to manage cars and their ratings.

## Technology Stack
* Django 
* Django Rest Framework
* SQLite

Django is a high-level web framework that comes with a wide range of built-in features such as authentication, admin interface, ORM, and a powerful routing system. This makes development faster as you don't need to reinvent the wheel for common web development tasks.

DRF is a flexible and powerful toolkit for building Web APIs in Django. It provides serializers for data serialization/deserialization, class-based views, authentication, pagination, and more, which simplifies API development.

SQLite is a lightweight, serverless, and self-contained database engine that requires minimal setup and administration. It's ideal for small to medium-sized projects or prototypes where simplicity and ease of use are priorities.

## Setup
To run this project:

```
$ git clone https://github.com/SypekKonrad/car-api.git
```
```
$ cd car-api
```
```
$ bash app_build.sh
```

## Endpoints

### POST /cars
This endpoint allows you to add a new car to the database based on its make and model name.

Request Body:
```
{
    "make": "string",
    "model": "string"
}

```
Response:
* 201 Created: If the car is successfully added to the database.
* 400 Bad Request: If the request body is invalid or incomplete.
* 404 Not Found: If the car make and model combination doesn't exist.

### POST /rate

This endpoint allows you to add a rating for a car from 1 to 5.

Request Body:
```
{
    "car_id": "integer",
    "rating": "integer (1-5)"
}
```
Response:
* 201 Created: If the rating is successfully added to the database.
* 400 Bad Request: If the request body is invalid or incomplete.


### GET /cars

This endpoint allows you to fetch a list of all cars present in the application database along with their current average rating.

Response:
```
[
    {
        "id": "integer",
        "make": "string",
        "model": "string",
        "average_rating": "float"
    },
]
```

### GET /popular

This endpoint returns the top cars already present in the database, ranked based on the number of ratings they have received.

Response:
```
[
    {
        "id": "integer",
        "make": "string",
        "model": "string",
        "number_of_ratings": "integer"
    },
]

```




