# Check if config file exists
ifeq (,$(wildcard argos/.env.development.local))
    $(error "Missing config file; please copy .env.example to .env.development.local, and update the values")
endif

# Compute docker tag
DOCKER_IMAGES=$(shell docker images -q argos-front 2> /dev/null)

ifeq ($(DOCKER_IMAGES), )
  DOCKER_TAG=0.01
else
  DOCKER_TAG=$(shell docker images | awk '($$1 == "argos-front") {print $$2 += .01; exit}')
endif

# Check if a port is given
REACT_PORT?=8888

install:
	npm install

build:
	docker build -t argos-front:latest -t argos-front:$(DOCKER_TAG) .

clean-docker:
	docker ps -a | awk '{ print $$1,$$2 }' | grep argos-front | awk '{print $$1 }' | xargs -I {} docker rm {}
	docker rmi $$(docker images --format '{{.Repository}}:{{.Tag}}' | grep 'argos-front')

run:
	docker run -it -p 0.0.0.0:$(REACT_PORT):3000 argos-front:latest