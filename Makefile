.PHONY: run_simulation_robot run_simulation_world

IMAGE_NAME=robot_simulation
TAG=latest

run_simulation_robot:
	xhost +local:docker

	docker build -t $(IMAGE_NAME):$(TAG) .

	docker run -it --rm \
		--net=host \
		--gpus all \
		-e DISPLAY=$$DISPLAY \
		-e QT_X11_NO_MITSHM=1 \
		-e NVIDIA_VISIBLE_DEVICES=all \
      	-e NVIDIA_DRIVER_CAPABILITIES=graphics,utility,compute \
		-v /tmp/.X11-unix:/tmp/.X11-unix:rw \
		-v ../robot_description_template/robot_description:/robot_simulation_ws/src/robot_description \
		$(IMAGE_NAME):$(TAG) 

	xhost -local:docker

run_simulation_world:
	xhost +local:docker

	docker build -t $(IMAGE_NAME):$(TAG) .

	docker run -it --rm \
		--net=host \
		--gpus all \
		-e DISPLAY=$$DISPLAY \
		-e QT_X11_NO_MITSHM=1 \
		-e NVIDIA_VISIBLE_DEVICES=all \
      	-e NVIDIA_DRIVER_CAPABILITIES=graphics,utility,compute \
		-v /tmp/.X11-unix:/tmp/.X11-unix:rw \
		-v ../robot_description_template/robot_description:/robot_simulation_ws/src/robot_description \
		$(IMAGE_NAME):$(TAG) \
		ros2 launch robot_simulation simulation_world.launch.py

	xhost -local:docker

	