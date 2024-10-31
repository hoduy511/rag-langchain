# Default target
.DEFAULT_GOAL := help

# Help target
help:
	@echo "Available commands:"
	@echo "  make up         - Start the application"
	@echo "  make down       - Stop the application"
	@echo "  make logs       - View application logs"
	@echo "  make shell      - Open a shell in the app container"
	@echo "  make clean      - Remove all containers and volumes"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linter"
	@echo "  make format     - Format code using autopep8"

# Start the application
up:
	docker-compose up -d

# Stop the application
down:
	docker-compose down

# View application logs
logs:
	docker-compose logs -f

# Open a shell in the app container
shell:
	docker-compose exec app /bin/bash

# Remove all containers and volumes
clean:
	docker-compose down -v
	docker system prune -af

# Run tests
test:
	pytest -v --disable-warnings

# Run linter
lint:
	flake8 app/ app/tests

# Format code using autopep8
format:
	autopep8 --in-place --aggressive --aggressive app/src/**/*.py
	autopep8 --in-place --aggressive --aggressive app/tests/**/*.py
	isort app/src/**/*.py
	isort app/tests/**/*.py

.PHONY: help up down logs shell clean test lint format
