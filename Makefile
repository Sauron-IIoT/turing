build:
	docker build -t turing .

run:
	docker run -it -p 8888:8888 turing