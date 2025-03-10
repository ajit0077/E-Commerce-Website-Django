# E-Commerce Website (Django)

This is an open-source eCommerce website project that allows users to browse, search, and purchase products online. The application is built with Django, providing a scalable and responsive platform for both customers and administrators.

## Features

- Product catalog with detailed descriptions
- User authentication and authorization
- Shopping cart functionality
- Secure payment processing with PayPal
- Order history and tracking
- Admin dashboard for managing products, orders, and users
- Responsive design for optimal user experience on various devices

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript, jQuery
- **Backend:** Django, Python
- **Database:** SQLite3
- **Payment Gateway:** PayPal

## Installation and Setup

### Prerequisites

Ensure you have the following installed on your system:

- Python (>= 3.8 recommended)
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Steps to Run the Project

#### 1. Clone the Repository
```bash
git clone https://github.com/ajit0077/E-Commerce-Website-Django.git
cd E-Commerce-Website-Django
```

#### 2. Create and Activate a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Apply Migrations
```bash
python manage.py migrate
```

#### 5. Create a Superuser (For Admin Access)
```bash
python manage.py createsuperuser
```
Follow the on-screen instructions to set up an admin account.

#### 6. Run the Development Server
```bash
python manage.py runserver
```
The project will be available at `http://127.0.0.1:8000/`.

#### 7. Access the Admin Panel
Go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials created earlier.

## Configuration

### PayPal Integration
To configure PayPal for payment processing:
1. Sign up for a PayPal developer account.
2. Obtain API credentials from your PayPal dashboard.
3. Update your settings in `settings.py`:
   ```python
   PAYPAL_RECEIVER_EMAIL = 'your-paypal-email@example.com'
   PAYPAL_TEST = True  # Set to False in production
   ```

### Static Files
To collect static files for production, run:
```bash
python manage.py collectstatic
```

## Deployment
For deployment, consider using:
- Gunicorn & Nginx (for production servers)
- Docker (for containerization)
- AWS, DigitalOcean, or Heroku for hosting

## Contributing
Contributions are welcome! If you'd like to contribute, follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a Pull Request


## Contact
For any queries or suggestions, feel free to contact:
- Email: ajitnawade007@gmail.com
- GitHub: [ajit0077](https://github.com/ajit0077)

---
Happy Coding! 🚀

