build:
	docker build -t auth-api .

run:
	docker run -p 8000:8000 auth-api