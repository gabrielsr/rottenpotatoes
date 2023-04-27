
# Add dependency
` poetry add Flask-SQLAlchemy `

# Initialize db

1. Instantiate SQLAlchemy in `models/__init__.py`
2. Bind app and db in webapp.py

# Access 

Use flask shell
`$ poetry run flask --app app/webapp shell  `


Create user
```
>>> 
>>>user = User(firstname="gab", lastname="rod", email="email", age=1)
>>>db.session.add(user)
>>>db.session.commit()
``` 

Use SQL Lite viewer to to see the newly created database, with user table and the new user.