### DOCKER

1. Start project's containers 'docker-compose up'
2. To rebuild container 'docker-compose build web'
3. To enter container 'docker exec -it {id} bash'
4. Listing available containers 'docker ps'

### Setup
To run this project:

```
1. Open project in IDE
2. Type in terminal 'docker-compose up'
3. Open new terminal and type 'docker ps'
4. Take first 4 digits from 'container id' in 'hex_api..' row
5. Type 'docker exec -it {id} bash'
6. Type python manage.py migrate
7. Open browser, paste http://0.0.0.0:8000/
```
