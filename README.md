# Python Flask JWT Ext Tutorial

This shows how to use JWT with Flask.

## Steps

- virtual env using pyenv virtualenv 3.9.2
- install flask, flask-jwt-extended
- install psycopg2 & psycopg2-binary (better for macs) to access postgres dB
- install flask-sqlalchemy to abstract sql
- install python-dotenv to manage secret keys
- gunicorn to deploy to linux servers like digitalocean or heroku
- create a .env file
- inside the .env file provide the following:
  - JWT_SECRET
  - POSTGRES_USERNAME
  - POSTGRES_PASSWORD
  - POSTGRES_URL
  - POSTGRES_PORT
- Create three files
  - factory.py
  - extensions.py
  - app.py

```bash
  from flask_jwt_extended import JWTManager
  from flask-sqlalchemy import SQLAlchemy
```

- inside extensions.py
  - instantiate two objects of JWTManager and SQLAlchemy

= inside factory

## Blueprints added

Blueprints were used to put everything inside the directory server.
Inside of the original app.py the app is in the directory 'server'.
Also __init__.py files had to be added to make python packages.

## References

[video](https://www.youtube.com/watch?v=pAOAhZNlGK8)
[On blueprints](https://exploreflask.com/en/latest/blueprints.html)
