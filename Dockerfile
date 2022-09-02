FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

EXPOSE 8000

# ENTRYPOINT ["/bin/bash", "/code/src/entrypoint.sh"]
# CMD ["uvicorn", "src.main:src", "--host", "0.0.0.0", "--port", "8000"]