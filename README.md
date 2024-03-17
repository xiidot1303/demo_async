uvicorn core.asgi:application --host 127.0.0.1 --port 8000
gunicorn --worker-class=gevent  --bind=127.0.0.1:8000 core.wsgi:application

Edit your PostgreSQL configuration file (postgresql.conf) and locate the max_connections setting.

