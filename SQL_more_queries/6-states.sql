-- Task 6:
-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the newly created or existing database
USE hbtn_0d_usa;

-- Create the table 'states' if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
