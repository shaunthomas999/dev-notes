# PostgreSQL 

## Installation - Server

### (1) Homebrew
* Install - `brew install postgresql@14`
  * At successful installation this message - 'This formula has created a default database cluster with: initdb --locale=C -E UTF-8 /opt/homebrew/var/postgres'
* `brew services list` - See which versions of postgresql have been installed and which version is running now
* To switch versions:
  * `brew services stop postgresql@14`
  * `brew services start postgresql@13`
  * `brew unlink postgresql@14`
  * `brew link postgresql@13`
  * `echo 'export PATH="/opt/homebrew/opt/postgresql@13/bin:$PATH"' >> ~/.zshrc`
* Initial setup
  * `createuser -s postgres` - create user postgres
  * `psql -U postgres` - login postgres user
* Binaries are in `/opt/homebrew/opt/postgresql@14/bin`
  * Default binaries `postgres` and `psql` are in `/opt/homebrew/bin` 
* Run not as daemon `/opt/homebrew/opt/postgresql@14/bin/postgres -D /opt/homebrew/var/postgresql@14`
* References
  * https://daily-dev-tips.com/posts/installing-postgresql-on-a-mac-with-homebrew/ 
  * https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3

#### Start & Stop manually
* `pg_ctl -D /usr/local/var/postgres start`
* `pg_ctl -D /usr/local/var/postgres stop`
* `pg_ctl -D /usr/local/var/postgres status`
  * `pg_ctl -D /opt/homebrew/var/postgresql@14 status` 
* `-D` - data directory
* If installed by @14 brew install command then data directory is in `/opt/homebrew/var/postgresql@14`
* More options > https://www.postgresql.org/docs/current/app-pg-ctl.html

#### Start & Stop automatically now & on login
* Start - `brew services start postgresql@14`
* Stop - `brew services stop postgresql@14`
* Restart - `brew services restart postgresql@14`

### (2) Docker / docker-compose
* Run commands
  * `docker pull postgres:16-alpine`
  * `docker run --name postgres16 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:16-alpine`
  * `docker exec postgres16 psql -U postgres -c "CREATE DATABASE testdb" postgres`
* Now connect from Intellij IDEA

_!! Make sure Homebrew is not running Postgresql on the same port locally !!_

* docker-compose
  * https://hub.docker.com/_/postgres
  * https://docs.docker.com/engine/examples/postgresql_service/
    * Good ref - docker-compose - Postgresql + pgAdmin - https://github.com/docker/awesome-compose/tree/master/postgresql-pgadmin
  
#### References
* Dockerfile - https://github.com/docker-library/postgres/blob/4edbda205c684c861e6fbf964de5d00845864d42/12/alpine/Dockerfile
* Default port - 5432
* Default volume - `/var/lib/postgresql/data`
* PSQL command - `psql -h localhost -p 5432 -d postgres -U postgres --password`
* Ref:
  * https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb

### (3) Postgres App 
* Download and install PostgreSQL app from https://postgresapp.com/
* Start the app and click Initialize button
* Then in the database shown, click on the one with name 'postgres'

### (4) Enterprise DB
* https://www.enterprisedb.com/postgres-tutorials/installation-postgresql-mac-os

## Installation - Client

### (1) pgAdmin 4
* https://www.pgadmin.org/
* Download or brew install --cask
  * https://www.pgadmin.org/download/pgadmin-4-macos/ 

### (2) Postico
* Mac native app
* Not that many features as pgAdmin
* More commerical than open source

### (4) dbweaver
* https://dbeaver.io/
* Eclipse based

### (3) pgWeb
* http://sosedoff.github.io/pgweb/

### Others
* https://pgdash.io/blog/postgres-gui-tools.html

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
* `CREATE ROLE "test-user" WITH LOGIN PASSWORD 'testdb';`
* `CREATE DATABASE "test-db" OWNER "test-user";`
* `CREATE SCHEMA "test-schema" AUTHORIZATION "test-db";`

#### Superuser

* `CREATE ROLE user_name SUPERUSER LOGIN PASSWORD 'password';`
* or
* `ALTER USER user_name WITH SUPERUSER;`


## PSQL (CLI)

* `\q` - quit
* `\l` - list all database
* `\du` - display all users & roles
* `\c` (`\connect`) - show current database or connect to database
  * `e.g. \c greetings-db`
* Tip: By default PSQL will show database name in the prompt

## pg_dump and pg_restore

* Location with brew install - `/opt/homebrew/Cellar/postgresql@14/14.5_5/bin/pg_dump`

## SQL
* https://www.postgresqltutorial.com/
  * See the menu links on the right side

## Postgresql database settings

### Server settings
* To see all server settings - `SELECT * FROM pg_settings;`
* Might have to reload/restart after config change*

### Client settings

#### pgAdmin
* `SHOW datestyle;` - See default datestyle. Default (ISO, MDY). Here MDY means MM-DD-YYYY. ISO is YYYY-MM-DD
* `SET datestyle = 'ISO, YMD';`

## Performance troubleshooting

* pgbadger - memory leak in database connection
* max_connections
  * `ALTER SYSTEM SET max_connections = <value>`
  * `SHOW max_connections;`
  * Change
    * `psql -U <admin_user> -d <database_name>` 
    * `ALTER SYSTEM SET max_connections = 500;`
    * `SELECT pg_reload_conf();` - To reload values in `/opt/homebrew/var/postgresql@14/postgresql.conf` file
  * Other option

```sql
SELECT name, setting
FROM pg_settings
WHERE name = 'max_connections';
```

## Monitoring
* https://sematext.com/blog/postgresql-monitoring/

## Process
* pg_stat_activity
  *  `SELECT * FROM pg_stat_activity;`
  * Find process running for more than 5 minutes
```sql 
SELECT pid, query, state, age(now(), query_start) AS "age"
FROM pg_stat_activity
WHERE state != 'idle' AND query_start < now() - interval '5 minute';
```

  * Terminate process running for more than 5 minutes
```sql
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state = 'active'
AND now() - query_start > interval '5 minutes';

//-- pg_cancel_backend(pid)
//-- state = 'idle'
//-- state != 'idle'
```

  * To find all blocking PIDs
```sql
select pid, 
       usename, 
       pg_blocking_pids(pid) as blocked_by, 
       query as blocked_query
from pg_stat_activity
where cardinality(pg_blocking_pids(pid)) > 0;
```

  * to terminate all these PIDs replace `pid` in the select query with `pg_terminate_backend(pid)`

## Special SQLs
* UUID generation - `uuid_in(overlay(overlay(md5(random()::text || ':' || random()::text) placing '4' from 13) placing to_hex(floor(random() * (11 - 8 + 1) + 8)::int)::text from 17)::cstring)`
* Timestamp - `NOW()::timestamp`
 
## Cheatsheets

* https://quickref.me/postgres
* https://postgrescheatsheet.com
* https://www.postgresqltutorial.com/postgresql-cheat-sheet/

## Versioning and upgrading
* Find version - `Select Version();`
* https://www.postgresql.org/support/versioning/
* https://www.postgresql.org/docs/current/upgrading.html
* https://www.postgresql.org/docs/current/pgupgrade.html

