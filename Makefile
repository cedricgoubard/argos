build:
	cd back && $(MAKE) build
	cd front && $(MAKE) build

run:
	docker-compose up