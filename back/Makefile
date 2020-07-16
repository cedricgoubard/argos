# Check if config file exists
ifeq (,$(wildcard ./config.yaml))
    $(error "Missing config file; please copy config.example.yaml to config.yaml, and update the values")
endif

# Check if a port is given
FLASK_PORT?=8888

# Compute docker tag
DOCKER_IMAGES=$(shell docker images -q argos-back 2> /dev/null)

ifeq ($(DOCKER_IMAGES), )
  DOCKER_TAG=0.01
else
  DOCKER_TAG=$(shell docker images | awk '($$1 == "argos-back") {print $$2 += .01; exit}')
endif

install:
	python3 -m venv venv
	venv/bin/pip install wheel
	venv/bin/pip install -r requirements.txt
	mkdir uploads
	#venv/bin/python -m ipykernel install --user --name=argos

uninstall:
	#venv/bin/python -m jupyter kernelspec uninstall argos
	rm --force --recursive venv/
	rm --forece --recursive uploads/

update-requirements:
	pip freeze | grep -v "pkg-resources" > requirements.txt

build:
	docker build -t argos-back:latest -t argos-back:$(DOCKER_TAG) .

clean-docker:
	docker ps -a | awk '{ print $$1,$$2 }' | grep argos-back | awk '{print $$1 }' | xargs -I {} docker rm {}
	docker rmi $$(docker images --format '{{.Repository}}:{{.Tag}}' | grep 'argos-back')

run:
	docker run -p $(FLASK_PORT):$(FLASK_PORT) -v uploads:/argos/uploads argos-back:latest

clean-python:
	rm --force --recursive *.egg-info
