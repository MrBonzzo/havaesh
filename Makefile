create_mongo:
	docker-compose -f ./infra/docker/docker-compose.yaml --env-file ./env/.env up --build -d

run_mongo:
	docker-compose -f ./infra/docker/docker-compose.yaml --env-file ./env/.env up --no-build -d

stop_mongo:
	docker-compose -f ./infra/docker/docker-compose.yaml stop

connect_to_mongo:
	docker exec -it havaesh_mongo_container /bin/bash

run_app:
	uvicorn src.app:app --reload --port 8080 --env-file ./env/.env

run_app_wo_env:
	uvicorn src.app:app --reload --port 8080
