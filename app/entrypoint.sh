#echo "Run alembic migrations"
#alembic upgrade head

echo "Run app"
uvicorn app.web.run_server:app --host 0.0.0.0 --port 8000