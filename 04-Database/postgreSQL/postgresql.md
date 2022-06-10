# PostgreSQL 

## Installation

### Postgres App 
* Download and install PostgreSQL app from https://postgresapp.com/
* Start the app and click Initialize button
* Then in the database shown, click on the one with name 'postgres'

### Enterprise DB
* https://www.enterprisedb.com/postgres-tutorials/installation-postgresql-mac-os

### Docker
* https://hub.docker.com/_/postgres
* https://docs.docker.com/engine/examples/postgresql_service/

### Homebrew
* Install - `brew install postgresql`
  * At successful installation this message - 'This formula has created a default database cluster with: initdb --locale=C -E UTF-8 /opt/homebrew/var/postgres'
* Start - `brew services start postgresql`
* Stop - `brew services stop postgresql`
* Interact - `psql postgres`
* References
  * https://daily-dev-tips.com/posts/installing-postgresql-on-a-mac-with-homebrew/ 
  * https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3

## Setup steps

### Docker

* Run commands
  * `docker pull postgres:12.3-alpine`
  * `docker run --name postgresqldb -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:12.3-alpine`
  * `docker exec postgresqldb psql -U postgres -c"CREATE DATABASE testdb" postgres`
* Now connect from Intellij IDEA

#### References
* Dockerfile - https://github.com/docker-library/postgres/blob/4edbda205c684c861e6fbf964de5d00845864d42/12/alpine/Dockerfile
* Default port - 5432
* Default volume - `/var/lib/postgresql/data`
* PSQL command - `psql -h localhost -p 5432 -d postgres -U postgres --password`


### Normal
* https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb
