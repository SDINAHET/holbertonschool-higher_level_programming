-- Task 7:
-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the newly created or existing database
USE hbtn_0d_usa;

-- Create the 'states' table if it doesn't exist to avoid foreign key constraint issues
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Create the 'cities' table if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
