

# 🛍️ E-Commerce Store

A comprehensive, full-fledged e-commerce platform built with **Django**, featuring secure **Stripe payment processing**, robust **product management**, and a **user-friendly interface**.

<img width="1920" height="903" alt="image" src="https://github.com/user-attachments/assets/2859084d-3efa-4b0c-a8d4-73d1e61d266d" />

---

## 📚 Table of Contents

* [Features](#features)
* [Technologies Used](#technologies-used)
* [Getting Started](#getting-started)

  * [Prerequisites](#prerequisites)
  * [Local Development Setup](#local-development-setup)
  * [Running Migrations](#running-migrations)
  * [Creating a Superuser](#creating-a-superuser)
  * [Running the Development Server](#running-the-development-server)
* [Stripe Integration](#stripe-integration)

  * [Setting up Stripe Webhooks](#setting-up-stripe-webhooks)
* [Deployment (cPanel / MySQL)](#deployment-cpanel--mysql)
* [Security Features](#security-features)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

---

## ✨ Features

This e-commerce store offers a complete set of functionalities expected from a modern online retail platform:

### 🛒 Product Management

* Add, edit, and delete products with descriptions, images, pricing, and stock levels.
* Categorization of products for easy navigation.
* Optional: Product variations (e.g., size, color).

### 🧺 Shopping Cart

* Add, update, and remove items in a persistent cart.

### 👤 User Authentication

* Secure registration, login, logout, and password management.

### 📦 Order Management

* Customers can view their order history.
* Admin panel for order tracking and management.

### 💳 Stripe Payment Integration

* Secure payments via credit/debit cards.
* **Stripe Webhooks** for tracking events like success, failure, or refunds.

### 🔍 Product Search

* Quick and efficient search across product listings.

### 📱 Responsive Design

* Mobile-first UI using **Bootstrap** and **Tailwind CSS**.

### ⚙️ Admin Panel

* Full access to manage users, products, and orders via **Django Admin**.

---

## 🛠️ Technologies Used

### Backend

* Python 3.x
* Django
* Django Crispy Forms *(optional)*
* Stripe Python SDK

### Frontend

* HTML5, CSS3, JavaScript
* Bootstrap 5
* Tailwind CSS

### Database

* SQLite (development)
* MySQL (production via cPanel)

### Version Control

* Git

---

## 🚀 Getting Started

### 📋 Prerequisites

Ensure you have these installed:

* Python 3.8+
* `pip`
* `git`

### 💻 Local Development Setup

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 🧪 Create a virtual environment

```bash
python -m venv venv
```

### ✅ Activate the virtual environment

**Windows:**

```bash
.\venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 🔐 Environment Variables

Create a `.env` file in the root:

```
SECRET_KEY=your_django_secret_key_here
DEBUG=True
STRIPE_PUBLISHABLE_KEY=pk_test_YOUR_KEY
STRIPE_SECRET_KEY=sk_test_YOUR_KEY
STRIPE_WH_SECRET=whsec_YOUR_KEY
```

---

## 🔃 Running Migrations

```bash
python manage.py migrate
```

---

## 👨‍💼 Creating a Superuser

```bash
python manage.py createsuperuser
```

Follow prompts to create an admin account.

---

## 🧪 Running the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 💳 Stripe Integration

This app uses **Stripe** for payment processing. To test webhooks and transactions:

### 🌐 Setting up Stripe Webhooks

1. **Install Stripe CLI**
   [Install Stripe CLI](https://stripe.com/docs/stripe-cli)

2. **Login:**

   ```bash
   stripe login
   ```

3. **Forward events:**

   ```bash
   stripe listen --forward-to http://localhost:8000/your-webhook-url/
   ```

4. **Update `.env`** with `STRIPE_WH_SECRET` provided by Stripe CLI.

---

## 🌍 Deployment (cPanel / MySQL)

### 📦 Configure MySQL in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 📤 Collect Static Files

```bash
python manage.py collectstatic
```

### ⚙️ Passenger WSGI (e.g., `passenger_wsgi.py`):

```python
import os, sys

sys.path.insert(0, os.path.dirname(__file__))
INTERP = os.path.join(os.environ['HOME'], 'path/to/venv/bin/python')
if sys.executable != INTERP:
    os.execv(INTERP, [INTERP] + sys.argv)

os.environ['DJANGO_SETTINGS_MODULE'] = 'your_project_name.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

---

## 🔐 Security Features

* **HTTPS**: Required for Stripe and all production use.
* **CSRF Protection**: Built-in with Django.
* **XSS Protection**: Output encoding via Django templates.
* **SQL Injection Protection**: Handled via Django ORM.
* **Environment Variables**: No hardcoded secrets.
* **Webhook Verification**: Stripe webhook secrets used for request verification.
* **Secure Passwords**: Django uses PBKDF2 with SHA256 by default.

---

## 🤝 Contributing

Contributions welcome!

```bash
# Fork and clone this repository
git checkout -b feature/YourFeatureName
# Make changes and commit
git commit -m "Add: YourFeatureName"
git push origin feature/YourFeatureName
# Open a Pull Request
```

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more details.

---

## 📬 Contact

**Muhammad Zain ul Abideen**
📧 [meher00zain@gmail.com](mailto:meher00zain@gmail.com)
🔗 [GitHub Project Link](https://github.com/MahrZain/babyplanet.git)

---

Would you like this saved as a `.md` file or automatically added to your repo (if linked)?
