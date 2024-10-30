-- Task 2:
-- Create the database 'hbtn_0d_2' if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user 'user_0d_2' with the specified password if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the 'hbtn_0d_2' database to 'user_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
