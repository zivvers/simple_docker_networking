# simple_docker_networking

*relevant commands*:

Build and stand-up containers

```
sudo docker-compose build 
sudo docker-compose up -d
```

Connect to running server container (run `python server.py` within container)

```
sudo docker exec -it $(sudo docker ps --filter name=server --filter status=running -aq) /bin/bash
```

Connect to running client container (run `python client.py` within container)

```
sudo docker exec -it $(sudo docker ps --filter name=client --filter status=running -aq) /bin/bash
```
