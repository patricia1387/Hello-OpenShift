import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))
os.environ['API_GREETINGS'] = 'greetings'

# Get environment variables
GREETINGS = os.getenv('API_GREETINGS')
forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
