.PHONY: build_robot_simulation_world \
		run_robot_simulation_world \
		stop_robot_simulation_world \
		connect_robot_simulation_world \
		build_robot_simulation_spawn \
		run_robot_simulation_spawn \
		stop_robot_simulation_spawn \
		connect_robot_simulation_spawn

build_robot_simulation_world:
	@docker compose build robot_simulation_world

run_robot_simulation_world:
	@docker compose up robot_simulation_world

stop_robot_simulation_world:
	@docker compose stop robot_simulation_world

connect_robot_simulation_world:
	@docker exec -it robot_simulation_world bash

build_robot_simulation_spawn:
	@docker compose build robot_simulation_spawn

run_robot_simulation_spawn:

	@docker compose up robot_simulation_spawn

stop_robot_simulation_spawn:
	@docker compose stop robot_simulation_spawn

connect_robot_simulation_spawn:
	@docker exec -it robot_simulation_spawn bash

