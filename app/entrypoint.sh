echo "Run alembic migrations"
alembic upgrade head

echo "Run app"
uvicorn app.main:app --host 0.0.0.0 --port 8000