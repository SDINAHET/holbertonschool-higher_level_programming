-- Task0:
-- Create users if they do not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- CREATE USER 'user_0d_1'@'localhost';
-- CREATE USER 'user_0d_2'@'localhost';

-- Grant privileges to each user if they don't have any (adjust privileges if necessary)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';
-- GRANT SELECT ON *.* TO 'user_0d_2'@'localhost'; -- Adjust as necessary

-- Show privileges for each user
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
