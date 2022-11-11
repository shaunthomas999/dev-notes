# PostgreSQL 

## Installation

### (1) Postgres App 
* Download and install PostgreSQL app from https://postgresapp.com/
* Start the app and click Initialize button
* Then in the database shown, click on the one with name 'postgres'

### (2) Enterprise DB
* https://www.enterprisedb.com/postgres-tutorials/installation-postgresql-mac-os

### (3) Docker
* https://hub.docker.com/_/postgres
* https://docs.docker.com/engine/examples/postgresql_service/

### (4) Homebrew
* Install - `brew install postgresql@14`
  * At successful installation this message - 'This formula has created a default database cluster with: initdb --locale=C -E UTF-8 /opt/homebrew/var/postgres'
* Interact
  * `createuser -s postgres` - create user postgres
  * `psql -U postgres` - login postgres user
* References
  * https://daily-dev-tips.com/posts/installing-postgresql-on-a-mac-with-homebrew/ 
  * https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3

#### Start & Stop manually
* `pg_ctl -D /usr/local/var/postgres start`
* `pg_ctl -D /usr/local/var/postgres stop`
* `pg_ctl -D /usr/local/var/postgres status`
* `-D` - data directory
* If installed by @14 brew install command then data directory is in `/opt/homebrew/var/postgresql@14`
* More options > https://www.postgresql.org/docs/current/app-pg-ctl.html

#### Start & Stop automatically now & on login
* Start - `brew services start postgresql`
* Stop - `brew services stop postgresql`

### (5) pgAdmin 4
* https://www.pgadmin.org/
* Download or brew install --cask
  * https://www.pgadmin.org/download/pgadmin-4-macos/ 

### (6) Postico
* Mac native app
* Not that many features as pgAdmin
* More commerical than open source

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

## Client tools

* pgAdmin 4 - Install from here - https://www.pgadmin.org/download/pgadmin-4-macos/

## Create Role and Database

### pgAdmin

* Start pgAdmin
* Create Role
  * Right-click 'Login/Group Roles' and select 'Create / Login/Group Role'
  * Enter 'Name' on the 'General' tab
  * Enter 'Password' on the 'Definition' tab
  * Select all privileges on the 'Privileges' tab
  * Click 'Save'
* Create Database
  * Right-click 'Databases' and select 'Create / Database'
  * Enter 'Database' on the 'General' tab
  * Enter 'Owner' on the 'General' tab
  * Click 'Save'

### CLI - psql tool

* `psql -U postgres` - Start psql
* `CREATE ROLE "test-db" WITH LOGIN PASSWORD 'testdb';`
* `CREATE DATABASE "test-db" OWNER "test-db";`

## PSQL

* `\q` - quit
* `\l` - list all database
* `\c` (`\connect`) - show current database or connect to database

## SQL
* https://www.postgresqltutorial.com/
  * See the menu links on the right side
 
## Cheatsheets

* https://quickref.me/postgres
* https://postgrescheatsheet.com
