release: python manage.py migrate
web: gunicorn todo.wsgi
daphne: daphne todo.asgi:application --port 6379 --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=todo.settings -v2

