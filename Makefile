# If the first argument is "set-port"...
ifeq (set-port,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "set-port"
  PORT_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(PORT_ARGS):;@:)
endif

install:
	curl -sL https://deb.nodesource.com/setup_12.x | sudo bash -
	sudo apt-get install -y nodejs python3-venv
	
	cd back && $(MAKE) install
	cd front && $(MAKE) install

	cp docker-compose.example.yaml docker-compose.yaml

	@echo  
	@echo "################################## NEXT STEPS ##################################"
	@echo 
	@echo Before building, you still need to fill in:
	@echo     - The back/config.yaml file
	@echo     - The front/argos/.env.development.local file
	@echo 
	@echo "################################################################################"

build:
	cd back && $(MAKE) build
	cd front && $(MAKE) build

run:
	docker-compose up

set-port:
	sed -i -r 's/port\: [0-9]{4,5}/port\: $(PORT_ARGS)/' back/config.yaml
	sed -i -r 's/(REACT_APP_BACK_URL = .{5,20})\:[0-9]{4,5}/\1\:$(PORT_ARGS)/' front/argos/.env.development.local
	sed -i -r 's/(.*)([0-9]{4,5})\:([0-9]{4,5})(.*Back Port, defined.*)/\1$(PORT_ARGS)\:$(PORT_ARGS)\4/' docker-compose.yml
