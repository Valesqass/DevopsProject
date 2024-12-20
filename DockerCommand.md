# DOCKER COMMAND

#### Construire/Démarrer un conteneur 
docker-compose up --build

### Voir les conteneurs actifs
docker ps

### Voir TOUS les conteneurs 
docker ps -a 


## DOCKER HUB

### Se connecter à DockerHub
docker login (username, password)

### Tager l'image docker 
docker tag {nom_du_conteneur} {username}/{nom_du_conteneur}:latest 

### Push dans le DockerHub
docker push {username}/{nom_du_conteneur}:latest