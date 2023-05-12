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

## Issues

After leaving the code for a while, returning found that the app was no longer working, unlike previously. From POSTMAN, I got the message 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'  I could see via pgAdmin that the server was indeed running so I will need to troubleshoot the code.

## References

[video](https://www.youtube.com/watch?v=pAOAhZNlGK8)

### On Posgres dB

- postgresql is deprecated -> postgresql@14
- start
  - brew services start postgresql
- stop
  - brew services stop postgresql
  - 