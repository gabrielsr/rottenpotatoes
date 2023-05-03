
# Install Dependencies
` poetry install` 

# Run App

` poetry run flask --app app/app run`
or
`poetry shell`
`flask --app app/app run`


# Run Flask Shell
`poetry run flask --app app/webapp shell`


# Admin DB 
Ref. https://flask-migrate.readthedocs.io/en/latest/
## Create a initial migration repository
`flask db init`
`flask db migrate -m "Initial migration."`
`flask db upgrade`

`flask admin seed`

## After updating the model
`flask db upgrade`

