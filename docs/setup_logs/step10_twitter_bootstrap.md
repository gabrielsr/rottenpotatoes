Ref.:
    https://bootstrap-flask.readthedocs.io/

 # Add dependency
 `poetry add bootstrap-flask`


 # Register Extension

Register the extension in `webapp.py`

```python
from flask import Flask
# To follow the naming rule of Flask extension, although
# this project's name is Bootstrap-Flask, the actual package
# installed is named `flask_bootstrap`.
from flask_bootstrap import Bootstrap5

# ...
app = Flask(__name__)
bootstrap = Bootstrap5(app)
```

# Add a base template 

added file in `tempaltes/base.html`


# Create an index that extends boostrap

` {% extends "base.html" %}` in `index.html`

# Rendering Template 

In the controller action (e.g., @app.get("/")) use render_template'

```python
    return render_template("index.html")
``` 