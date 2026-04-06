build:
	docker build -t auth-api .

run:
	docker run -p 8000:8000 auth-api

run-dev-without-docker:
	uvicorn app.main:app --reload

test:
	pytest -vv --tb=long
