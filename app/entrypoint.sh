echo "Repository type is ${REPOSITORY_TYPE}"
if [ "${TYPE}" == "postgres" ]
    then ./app/wait-for-it.sh -t 2 ${DB_HOST}:${DB_PORT} -- echo "DB is up"
fi

echo "Run alembic migrations"
alembic upgrade head

echo "Run app"
uvicorn app.main:app --host 0.0.0.0 --port 8000