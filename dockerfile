version: '3.8'

services:
  mongo1:
    container_name: mongo1
    hostname: mongo1
    image: mongo:6.0.3
    expose:
      - 27017
    ports:
      - 30001:27017
    restart: always
    networks:
      - mongoCluster
    command: mongod --replSet myrs
  mongo2:
    container_name: mongo2
    hostname: mongo2
    image: mongo:6.0.3
    expose:
      - 27017
    ports:
      - 30002:27017
    restart: always
    networks:
      - mongoCluster
    command: mongod --replSet myrs
  mongo3:
    container_name: mongo3
    hostname: mongo3
    image: mongo:6.0.3
    expose:
      - 27017
    ports:
      - 30003:27017
    restart: always
    networks:
      - mongoCluster
    command: mongod --replSet myrs

  mongoinit:
    container_name: mongoinit
    image: mongo:6.0.3
    restart: "no"
    networks:
      - mongoCluster
    depends_on:
      - mongo1
      - mongo2
      - mongo3
    command: >
      mongosh --host mongo1:27017 --eval  ' db = (new Mongo("localhost:27017")).getDB("myDb"); config = { "_id" : "myrs", "members" : [
        {
          "_id" : 0,
          "host" : "mongo1:27017"
        },
        {
          "_id" : 1,
          "host" : "mongo2:27017"
        },
        {
          "_id" : 2,
          "host" : "mongo3:27017"
        }
      ] }; rs.initiate(config); '


networks:
  mongoCluster:
    driver: bridge
