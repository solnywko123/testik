
Simple Inventory Management System with RESTful API
Project Overview
This application was developed as part of the Reviro TechStart internship - Spring 2024. It provides the ability to manage information about products and establishments through a RESTful API.

Instructions for Building and Running the Application using Docker Compose
Clone the repository:

git clone (https://github.com/solnywko123/testik)
cd testik
Build and start the containers using Docker Compose:

docker-compose up --build

Apply migrations to create tables in the database:
docker-compose exec web python manage.py migrate

Quick Guide to API Usage
Establishments
GET /establishments/: Get a list of all establishments.
GET /establishments/{id}/: Get information about a specific establishment.
POST /establishments/: Create a new establishment.
PUT /establishments/{id}/: Update information about an establishment.
DELETE /establishments/{id}/: Delete an establishment.
Products
GET /products/: Get a list of all products.
GET /products/{id}/: Get information about a specific product.
POST /products/: Create a new product.
PUT /products/{id}/: Update information about a product.
DELETE /products/{id}/: Delete a product.

For examples of requests and responses, refer to the Swagger documentation at http://0.0.0.0:8000/docs/.

Run the following command to execute tests in Docker:
docker-compose exec web pytest

The application uses PostgreSQL as the database, and the settings are configured in the settings.py file.

Results
Source Code: git.com/solnywko123/testik
Dockerfile and docker-compose.yml: Included in the repository
Swagger Documentation: http://localhost:8000/docs/
README: Included in the repository
Set of Module Tests: Included in the repository









