#!/bin/bash

# Atualização do sistema
sudo yum update -y
sudo yum install -y docker
sudo amazon-linux-extras enable docker
sudo service docker start
sudo systemctl start docker
sudo systemctl enable docker

# Download da imagem do DockerHub
docker pull image:latest

# Criação da rede e dos containers sem o compose
docker network create gpt_parsing_default
docker run -d --name redis --network gpt_parsing_default -p 6379:6379 redis:7
docker run -d --name listener --network gpt_parsing_default -p 8000:8000 image:latest
docker run -d --name celery_worker1 --network gpt_parsing_default image:latest celery -A tasks worker --loglevel=info
