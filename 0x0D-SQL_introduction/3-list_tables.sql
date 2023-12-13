-- This script list all tables in the specified database

USE `mysql`;

-- Retrieve table names from the information_schema.tables
SELECT table_name AS Tables_in_mysql
FROM information_schema.tables
WHERE table_schema = DATABASE();

