Ref.: 
https://flask.palletsprojects.com/en/2.3.x/tutorial/views/#create-a-blueprint


# Setting Session Key

Ref. https://flask-session.readthedocs.io/en/latest/#quickstart

This is needed for forms
```python
    app.config.from_mapping(
        SECRET_KEY="dev",
    )
    app.config.from_prefixed_env()
```

# create auth module
\controllers
  |- auth.py
\templates
  \- auth
    |- login.html
    |- register.html


# Register a blueprint in webapp.py

```python
    from .controllers.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
```