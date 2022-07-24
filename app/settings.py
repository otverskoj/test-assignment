import os


REPOSITORY_TYPE = os.environ.get('REPOSITORY_TYPE', 'in_memory').strip()

# DB SETTINGS
DB_HOST = os.environ.get('DB_HOST').strip()
DB_PORT = os.environ.get('DB_PORT', "5432").strip()
DB_USER = os.environ.get('DB_USER').strip()
DB_NAME = os.environ.get('DB_NAME').strip()
DB_PASSWORD = os.environ.get('DB_PASSWORD').strip()
