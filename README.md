# Guide

### Build and Run
```
docker-compose build
docker-compose up
```

### Create Flask migrations
```
flask db init
flask db migrate -m <migration-message>
flask db upgrade
```