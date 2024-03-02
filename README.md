# Guide

### Build and Run
```
docker-compose build
docker-compose up
```

### Add React Native dependencies
```
npm install <package-name> --save-prod
npm i --package-lock-only
```

### Create Flask migrations
```
flask db init
flask db migrate -m <migration-message>
flask db upgrade
```