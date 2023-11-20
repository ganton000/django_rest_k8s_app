.PHONY: start build down setup deploy-k8 delete-k8 deploy-k8-services delete-k8-services exec-k8 do-build secret secret-key kube-secret-create kube-secret-delete

start:
	docker-compose up -d

build:
	docker-compose up --build -d

down:
	docker-compose down

lint:
	poetry run mypy ./app

setup:
	export KUBECONFIG=$(pwd)/.kube/kubeconfig.yaml

deploy-k8: setup
	kubectl apply -f k8s/apps/deployment.yaml && kubectl get deployments && kubectl get pods

delete-k8: setup
	kubectl delete -f k8s/apps/deployment.yaml && kubectl get deployments && kubectl get pods

deploy-k8-services: setup
	kubectl apply -f k8s/nginx/service.yaml && kubectl get service

delete-k8-services: setup
	kubectl delete -f k8s/nginx/service.yaml && kubectl get service

exec-k8: setup
	kubectl exec -it $(POD_NAME) -- /bin/bash

do-build:
	docker build -t registry.digitalocean.com/anton-k8s/django-app-k8s:latest -f Dockerfile . && docker push registry.digitalocean.com/anton-k8s/django-app-k8s --all-tags

secret:
	@python -c "import secrets;print(secrets.token_urlsafe(32))"

secret-key:
	@python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

kube-secret-create: setup
	@kubectl create secret generic $(NAME) --from-env-file=app/.env.prod &&
	kubectl get secret $(NAME) -o YAML

kube-secret-delete: setup
	@kubectl delete secret $(NAME) && kubectl get secret
