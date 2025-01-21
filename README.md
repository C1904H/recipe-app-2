# Recipe App

## Overview

The Recipe App is a web application built using Python and the Django Framework. It is a dynamic, multi-user application, letting users sign up and create their own content. Users can create, read, modify recipes and search for recipes based on ingredients. There is also an admin panel for data handling and visualization.

## User Goals
Users can:
- Create and modify recipes containing ingredients, cooking time, description and a difficulty parameter automatically calculated by the application.
- Search for recipes by recipe name, ingredients or difficulty level.

## Key Features
- Allows for user authentication, login and logout
- Lets users search for recipes according to ingredients, difficulty level or recipe name
- App automatically rates each recipe by difficulty level
- Receives user input and handle errors appropriately
- Displays more details on each recipe if the user requests it
- Adds user recipes to an SQLite database
- Includes a Django Admin dashboard for working with database entries
- Shows statistics and visualizations based on trends and data analysis.

## Technical Requirements
- Python 3.6+ and Django 3 compatibility
- Exception handling with user-friendly error messages
- PostgreSQL for production and SQLite for development database connectivity
- Easy-to-use interface with simple input forms and easy to follow instructions
- Code documentation and automated tests hosted on GitHub (includes "requirements.txt" for easy project setup).
- Cloudinary for database media images

## Set Up and Installation
1. **Clone the Repository**
```
git clone <https://github.com/C1904H/recipe-app-2>
```

2. **Create and Activate Virtual Environment**  
```
python -m venv venv

# For Linux Based OS or Mac OS
source venv/bin/activate

# For Windows with CMD
.\venv\Scripts\activate.bat
```

3. **Install Dependencies**
```
pip install -r requirements.txt
```

4. **Setup Database**  
Adjust the DATABASES configuration in `settings` for PostgreSWL and SQLite as per your development and production environments.

5. **Run Migrations**

6. **Create Superuser for Admin Access**

7. **Run the Development Server**

8. **View on Local Host**  
Visit `http://127.0.0.1:8000 `in your browser to view app.

## Deployment
This application is deployed on Railway at [recipe-app-2-production.up.railway.app](https://recipe-app-2-production.up.railway.app/).

## Collaboration
Thanks to my Mentor Eyongkevin for django-boilerplate provision [GitHub link](https://github.com/Eyongkevin/django-boilerplate).