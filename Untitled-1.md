# Flashlink - Digital Business Card Website

Flashlink is a digital business card website built using Django. It allows users to create and share digital business cards with personalized contact information, social media profiles, and more. The app integrates PostgreSQL for data storage and Bulma for styling.

## Features

- **User Authentication**: Users can create an account, log in, and manage their business cards.
- **Custom Business Cards**: Users can input their contact details, including phone numbers, emails, social media links, and more.
- **Responsive Design**: Bulma is used for a responsive, modern design that works well on both mobile and desktop.
- **PostgreSQL Database**: The app uses PostgreSQL for reliable data storage.

## Requirements

- Python 3.11+
- PostgreSQL 16+
- pip (Python package installer)
- poetry

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <your-repository-url>
cd flashlink
```

### 2. Install Dependencies

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set Up PostgreSQL

Create a PostgreSQL database for the project. You can use the following commands to create a new database:

```bash
sudo -u postgres psql
CREATE DATABASE flashlink;
CREATE USER flashlink_user WITH PASSWORD 'yourpassword';
ALTER ROLE flashlink_user SET client_encoding TO 'utf8';
ALTER ROLE flashlink_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE flashlink_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE flashlink TO flashlink_user;
```

Update the `DATABASES` configuration in `flashlink/settings.py` with your PostgreSQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'flashlink',
        'USER': 'flashlink_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Apply Migrations

Run migrations to set up the database schema:

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

### 6. Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to access the app.

## Styling with Bulma

Bulma is included in the project for styling. It is integrated through the static files and can be used in any template by adding the appropriate classes.

## Deployment

For production deployment, consider using:

- **Gunicorn** as the WSGI server.
- **Nginx** as the reverse proxy.

Ensure your database and static files are properly configured for production.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
