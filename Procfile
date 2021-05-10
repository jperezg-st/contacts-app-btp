web: gunicorn contacts-app-btp.wsgi --log-file -
python manage.py collectstatic --noinput
manage.py migrate