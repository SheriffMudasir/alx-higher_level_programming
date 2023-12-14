-- This script creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create table states
CREATE TABLE IF NOT EXISTS states ( id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(256) NOT NULL);

