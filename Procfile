web: daphne -b 0.0.0.0 -p $PORT todo.asgi:application
worker: uvicorn todo.wsgi:application --port $PORT
