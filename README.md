# System for tracking ELO
A simple web app for tracking elo. Suports adding users (without authentification) and recording results of two player matches of a single game. Does not perform any type of rules validation, such as validating the result scores.

# Instalation
## Set environment variables
set the following environment variables

+ FLASK_APP : must be 'elo'
+ FLASK_ENV : must be 'development'
+ APP_ENVIRONMENT : must be 'development'
+ SECRET_KEY
+ DATABASE_URL : uri of the database. Can be an absolute path to sqlite db (sqlite:///path/to/db)

## Migrate database
```
flask db init
flask db migrate
flask db upgrade
'''

## Start server
```
flask run
```