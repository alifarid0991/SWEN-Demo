# SWEN

#### Commands to run project :

```bash
docker build -t my-py-mongo .
docker run --name my-py-mongo --restart=always -d -p 8080:8080 -p 27017:27017 -v $PWD/srv:/srv py-mongo mongod --auth
docker exec -i -t my-py-mongo 
cd /srv/swen && python3 manage.py runserver 0.0.0.0:8080
```
