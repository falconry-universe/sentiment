IMG=bert
MODELIMG=${IMG}-model

build:
	@docker build -t ${IMG} .

run:
	-@docker rm --force bert
	@docker run -d --name=bert -p 7860:7860 ${IMG}