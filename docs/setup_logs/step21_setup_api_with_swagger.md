
Ref. 
    https://flask-restx.readthedocs.io

# Include Flask RestX
`poetry add flask-restx`

# Create Blueprint and Resource
`/api
 |- reviews.py`

# Register api blueprint
`app/webapp.py`
'''
    # register api blueprint 
    from .api import blueprint as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')
'''

