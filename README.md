# Dependencies
`poetry` 
Ref. https://python-poetry.org

# Install Dependencies
`poetry install` 

# Run App

` poetry run flask --app app/webapp run`
or
`poetry shell`
`flask --app app/webapp run`


# Run Flask Shell
`poetry run flask --app app/webapp shell`

Or
`poetry shell`
`export FLASK_APP=app.webapp`
`flask run`


# Admin DB 
Ref. https://flask-migrate.readthedocs.io/en/latest/
## Create a initial migration repository
`flask db init`
`flask db migrate -m "Initial migration."`
`flask db upgrade`

`export FLASK_APP=app.webapp`
`flask seed movies`
`flask seed users`

## After updating the model
`flask db upgrade`

## "Hard Reset": Remove DB, initialize and reseed

`rm -f app/data.sqlite && rm -rf migrations && flask db init && flask db migrate -m "init" && flask db upgrade  && flask seed users && flask seed reviews && flask seed movies`