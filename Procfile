web: python manage.py collectstatic --noinput && python init_db.py && gunicorn rkventures_site.wsgi:application --bind 0.0.0.0:$PORT
