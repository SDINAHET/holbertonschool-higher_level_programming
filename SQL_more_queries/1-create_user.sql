-- Task 1:
-- Create user 'user_0d_1' with the specified password if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to 'user_0d_1' on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;
