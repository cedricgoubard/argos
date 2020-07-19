install:
	curl -sL https://deb.nodesource.com/setup_12.x | sudo bash -
	sudo apt-get install -y nodejs python3-venv
	
	cd back && $(MAKE) install
	cd front && $(MAKE) install

build:
	cd back && $(MAKE) build
	cd front && $(MAKE) build

run:
	docker-compose up