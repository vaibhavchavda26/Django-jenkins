docker stop $(docker ps -q  --filter ancestor=django_jenkins)
docker build -t django_jenkins .
docker run -d --restart=on-failure:5 --network=host -v $(pwd)/:/app/ django_jenkins
