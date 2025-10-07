# 🛍️ E-commerce Product API

## Description
A Django REST API for managing products and users in an e-commerce platform.

## Features
- CRUD for Users and Products
- Search products by name or category
- Django ORM for database management
- Deployed on Heroku/PythonAnywhere

## Endpoints
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET/POST | /api/users/ | List or create users |
| GET/PUT/DELETE | /api/users/{id}/ | Retrieve, update or delete a user |
| GET/POST | /api/products/ | List or create products |
| GET/PUT/DELETE | /api/products/{id}/ | Retrieve, update or delete a product |
| GET | /api/products/?search={query} | Search products by name or category |

## Installation
```bash
git clone https://github.com/Jooleric/ecommerce-product-api.git
cd ecommerce-product-api
pip install -r requirements.txt
python manage.py runserver
