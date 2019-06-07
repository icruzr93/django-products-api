type=$1
fails=''

inspect() {
    if [ $1 -ne 0 ]; then
        fails="${fails} $2"
    fi
}

server() {
    docker-compose up -d --build
    docker-compose exec api python manage.py test
    inspect $? users
    docker-compose down
}

e2e() {
    docker-compose -f docker-compose.prod.yml up -d --build
    docker-compose -f docker-compose.prod.yml exec api python manage.py test
    inspect $? e2e
    docker-compose -f docker-compose.prod.yml down
}

if [[ "${type}" == "server" ]]; then
    echo "\n"
    echo "Running server-side tests! \n"
    server
elif [[ "${type}" == "e2e" ]]; then
    echo "\n"
    echo "Running e2e-side tests! \n"
    e2e
else
    echo "\n"
    echo "Running all tests! \n"
    server
    e2e
fi

if [ -n "${fails}" ]; then
    echo "\n"
    echo "Tests failed ${fails}"
    exit 1
else
    echo "\n"
    echo "Tests passed!"
    exit 0
fi
