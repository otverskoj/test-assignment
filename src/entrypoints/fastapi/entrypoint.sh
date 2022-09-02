echo "Run alembic migrations"
alembic upgrade head

echo "Run app"
python3 main.py