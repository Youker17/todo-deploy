release: python manage.py migrate
web: gunicorn todo.wsgi
dapne: daphne todo.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=todo.settings -v2

