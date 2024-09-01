# 🛠️ Django Product and Lead Management API

Welcome to the Django Product and Lead Management API project! This project includes a RESTful API for managing products and leads, with full CRUD operations, reporting, and more.

## 📋 Table of Contents
1. [🔧 Installation](#installation)
2. [⚙️ Setup](#setup)
3. [📂 Endpoints](#endpoints)
4. [🎨 Frontend Development](#frontend-development)
5. [🔍 Testing](#testing)
6. [📄 License](#license)

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
Retrieves a list of all products.
* Retrieve Product: GET /api/products/{id}/
* Retrieves a single product by its ID.
* Create Product: POST /api/products/
* Creates a new product.
* Update Product: PUT /api/products/{id}/
* Updates an existing product by its ID.
   
   
   

