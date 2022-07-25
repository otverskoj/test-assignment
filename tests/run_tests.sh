#!/bin/bash

export $(cat ./app.test.env | grep REPOSITORY*)

if [ "$REPOSITORY_TYPE" == 'db' ]
    then docker-compose -f ./docker-compose-test.yaml up --build -d
fi

echo 'Run tests'
docker-compose -f ./docker-compose-test.yaml exec app pytest .

docker-compose -f ./docker-compose-test.yaml down -v