# PRODUCTS API

This application was made with django restframework, postgresql, nginx, docker and docker compose. Client in react pending.

## Reviewing API

Go To http://127.0.0.1/api/products/ to create products or to list all the products (GET, POST)

Or To http://127.0.0.1/api/products/:id/ to get, update or delete a specific product

You can enter to the admin going to this address http://127.0.0.1/admin, get the superuser credentials (DJANGO_SU_NAME, DJANGO_SU_PASSWORD) from the docker-compose files.

## Running Project

### Development

```sh
docker-compose up -d --build
```

### Production Environment

```sh
docker-compose -f docker-compose.prod up -d --build
```

## Testing Cases

### Test All

```sh
sh test.sh
```

### Test E2E

```sh
sh test.sh e2e
```

### Test API

```sh
sh test.sh api
```

### Manual testing

```sh
docker-compose up -d --build
docker-compose exec api python manage.py test
```
