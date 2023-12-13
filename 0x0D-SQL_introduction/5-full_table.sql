-- This script prints full description of first_table
USE `hbtn_0c_0`;

SELECT TABLE_NAME AS 'Table', CREATE_TABLE
FROM information_schema.tables
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table';

