create_infra:
	docker-compose -f ./docker-compose.yaml --env-file ./env/.env up --build -d

run_infra:
	docker-compose -f ./docker-compose.yaml --env-file ./env/.env up --no-build -d

stop_infra:
	docker-compose -f ./docker-compose.yaml stop

connect_to_mongo:
	docker exec -it havaesh_mongo_container /bin/bash

run_app:
	uvicorn src.app:app --reload --port 8080 --env-file ./env/.env
