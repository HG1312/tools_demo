# orders-service

Internal microservice that accepts and stores customer orders. Node API gateway
in front of a small Python (Flask) worker. PostgreSQL for storage.

## Run
docker build -t orders-service . && docker run -p 8000:8000 orders-service
