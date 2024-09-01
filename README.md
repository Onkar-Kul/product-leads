# 🛠️ Django Product and Lead Management API

Welcome to the Django Product and Lead Management API project! This project includes a RESTful API for managing products and leads, with full CRUD operations, reporting, and more.

## 📋 Table of Contents
1. [🔧 Installation](#installation)
2. [⚙️ Setup](#setup)
3. [📂 Endpoints](#endpoints)
4. [🎨 Frontend Development](#frontend-development)
5. [🔍 Testing](#testing)
6. [📄 Future Enhancement](#future-enhancement)

## 🔧 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Onkar-Kul/product-leads.git
   cd your-repository

2. **Create Virtual Environment**
   ```bash
    python -m venv venv
    source venv/bin/activate  
    # On Windows: venv\Scripts\activate

3. **Install all dependencies**
   ```bash
   pip install -r requirements.txt

## ⚙️ Setup

1. **Create Migrations**
   ```bash
   python manage.py makemigrations

2. **Apply migrations**
   ```bash
   python manage.py migrate

3. **Create Superuser**
   ```bash
   python manage.py createsuperuser

4. **Run Server**
   ```bash
   python manage.py runserver

## 📂 Endpoints
### Products
* __List Products__: GET /api/products/ 
  * Retrieves a list of all products.
* __Retrieve Product__: GET /api/products/{id}/
  * Retrieves a single product by its ID.
* __Create Product__: POST /api/products/
  * Creates a new product.
* __Update Product__: PUT /api/products/{id}/
  * Updates an existing product by its ID.

### Leads
* __Leads Create__: POST /api/products/
  * Creates a new Leads.

### Reporting APIs
* __Top Ten Products__: GET /api/product/top-ten-products/
  * Retrieves a list of top ten products.
* __Bottom Ten Product__: GET /api/product/bottom-ten-products/
  * Retrieves a list of bottom ten products.
* __Fetch Leads Between Two Dates__: GET api/lead/leads-between-dates/?start_date=&end_date=
  * Fetches Leads Between Two Dates.
* __Number of Products Inquired by Each Lead__: GET /api/lead/products-count/
  * Get Number of Products Inquired by Each Lead.
   
### User
* __User Registration for authentication__: POST /api/user/registration/ 
  * Register Users 
* __Login__: POST /api/user/login/
  * For login 
* __Logout__: POST /api/user/logout/
  * For logout.

## 🎨 Frontend Development
### 1. Create HTML Templates

* templates directory contains HTML files for the frontend.
Add CSS Styles

### 2. Create Static Files
* In static, css directory contains CSS files.

* In static, js directory contains JavaScript files for interactivity.

## 🔍 Testing
* Used Postman for testing all the APIs

## 📄 Future Enhancement
Future enhancements could focus on several areas to improve functionality, user experience, and scalability.
For example Pagination can be implemented, Security enhancement strong authentication and authorization mechanism like 
Jwt configuration can be improved like jwt rotation
