import os


REPOSITORY_TYPE=os.environ.get('REPOSITORY_TYPE', 'in_memory')

# DB SETTINGS
DB_HOST=os.environ.get('DB_HOST')
DB_PORT=os.environ.get('DB_PORT')
DB_USER=os.environ.get('DB_USER')
DB_NAME=os.environ.get('DB_NAME')
DB_PASSWORD=os.environ.get('DB_PASSWORD')
