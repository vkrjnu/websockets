web: python manage.py makemigrations --noinput
web: python manage.py migrate --noinput
web: manage.py runserver 0.0.0.0:80
heroku ps:scale web=1
