# Check if config file exists
ifeq (,$(wildcard ./config.yaml))
    $(error "Missing config file; please copy config.example.yaml to config.yaml, and update the values")
endif

DOCKER_IMAGES=$(shell docker images -q argos 2> /dev/null)

ifeq ($(DOCKER_IMAGES), )
  DOCKER_TAG=0.01
else
  DOCKER_TAG=$(shell docker images | awk '($$1 == "argos") {print $$2 += .01; exit}')
endif

install:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
	#venv/bin/python -m ipykernel install --user --name=argos

uninstall:
	#venv/bin/python -m jupyter kernelspec uninstall argos
	rm --force --recursive venv/

build:
	docker build -t argos:latest -t argos:$(DOCKER_TAG) .

clean-docker:
	docker ps -a | awk '{ print $$1,$$2 }' | grep argos | awk '{print $$1 }' | xargs -I {} docker rm {}
	docker rmi $$(docker images --format '{{.Repository}}:{{.Tag}}' | grep 'argos')

run:
	docker run -p 8374:8374 argos:latest

clean-python:
	rm --force --recursive *.egg-info
