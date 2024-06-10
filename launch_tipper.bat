@ECHO off

call ./env/Scripts/activate.bat

start "" /b python manage.py runserver

start "" /b npm run LaughLoud
