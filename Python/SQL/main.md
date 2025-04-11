
## CREATE USER
  CREATE USER name WITH PASSWORD 'xxxx'

## CREATE SUPERUSER
CREATE USER name WITH PASSWORD 'xxxx' SUPERUSER
ALTER USER name WITH SUPERUSER

## DELETE USER
 DROP USER name;
 DROP USER username;

## creating a superuser in SQL
sudo adduser abnas

## entering the database
sudo -u abnas psql

## GRANT PRIVILEGES TO SUPERUSER
ALTER USER johndoe WITH CREATEDB;        -- allow user to create databases
ALTER USER johndoe WITH SUPERUSER;       -- make user a superuser (⚠️ use with caution)
GRANT ALL PRIVILEGES ON DATABASE your_db TO johndoe; -- grant access to a specific DB
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO johndoe; -- grant access to all tables in a specific schema