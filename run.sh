#!/bin/sh

case "$1" in

  tests)
    docker build -t some_tt .
    docker network create some_tt
    docker run --network some_tt --name mongo -d mongo:4.4
    docker run --network some_tt --name some_tt -ti some_tt bash -c 'WAIT_HOSTS=mongo:27017 waitc && python3.7 -m some_tt & WAIT_HOSTS=some_tt:8080 waitc && pytest -vv'
    sh run.sh cleanup
    ;;

  cleanup)
    docker rm -f mongo some_tt
    docker network rm some_tt
    ;;

  *)
    docker build -t some_tt .
    docker network create some_tt
    docker run --network some_tt --name mongo -d mongo:4.4
    docker run --network some_tt --name some_tt -d -p "8080:8080" some_tt bash -c 'WAIT_HOSTS=mongo:27017 waitc && python3.7 -m some_tt'
    echo Please open http://127.0.0.1:8080/docs in browser
    ;;

esac