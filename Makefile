APP = restapi

flake: 
	@flake8 . --exclude .venv

compose:
	@docker compose build
	@docker compose up

test:
	@pytest --disable-warnings