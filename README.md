# Django Ecommerce

A simple Django Ecommerce project built with **Django**.

## Project Structure

- `ecommerce/` → Django project settings  
- `products/` → App for products and categories  
- `accounts/` → App for user authentication (login, signup)  
- `cart/` → App for shopping cart  
- `orders/` → App for managing orders  
- `templates/` → HTML templates  
- `static/` → Static files  
- `products/fixtures/products.json` → Predefined categories and products  

## Features

- Product listing by category  
- User authentication (signup/login/logout)  
- Shopping cart functionality  
- Order management  
- Admin panel for managing products and categories

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AykutYurekli/django-ecommerce.git
   cd django-ecommerce

Create and activate a virtual environment: python -m venv venv

Install Django: pip install django

Create a superuser for admin access: python manage.py createsuperuser

Run the development server: python manage.py runserver

Access the admin panel at: http://127.0.0.1:8000/admin/

Log in with the superuser account you created.

To add initial products and categories, load the provided fixtures: python manage.py loaddata products/fixtures/products.json

This will populate your database with predefined categories such as: Shoe, Hat, T-Shirt, Accessories, Pant, Beret, Sweatshirt, Shirt, Short

And products such as: Sneaker, Boot, Casual Shoe, Baseball Cap, Red Cap, Cowboy Hat, Beret, Blue Shirt, T-Shirts, Sweatshirts, Glasses, Ring, Scarf, Wristwatch

Usage: Visit the homepage at: http://127.0.0.1:8000/home

Users can: Register & log in
