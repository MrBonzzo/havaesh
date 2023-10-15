create_mongo:
	docker-compose -f ./infra/docker/docker-compose.yaml up --build -d

run_mongo:
	docker-compose -f ./infra/docker/docker-compose.yaml up --no-build -d

stop_mongo:
	docker-compose -f ./infra/docker/docker-compose.yaml stop

connect_to_mongo:
	docker exec -it havaesh_mongo_container /bin/bash
