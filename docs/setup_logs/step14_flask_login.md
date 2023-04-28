Ref.: https://www.freecodecamp.org/news/how-to-authenticate-users-in-flask/

# Install dependency

poetry add flask-login
poetry add flask-migrate
poetry add email_validator
poetry add flask-migrate

# Initialize extensions in webapp

Creating module auth

|- auth
 \_ controller.py
 \_ forms.py
 \_ loader.py

 Controllers  - MVC controller for login, logout, register and profile view
 Forms  - Forms used in auth
 Loaders - Put the logged in user in the request
 
# Create Migration

 `python manage.py` 



