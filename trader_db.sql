
-- Create Database
CREATE DATABASE IF NOT EXISTS trader_db;

-- Use the database
USE trader_db;

-- Create User (make sure to have necessary privileges)
-- CREATE USER 'trader_user'@'localhost' IDENTIFIED BY 'mysql@123';
-- GRANT ALL PRIVILEGES ON trader_db.* TO 'trader_user'@'localhost';

-- Create UserProfile table
CREATE TABLE IF NOT EXISTS tradeapp_userprofile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    email VARCHAR(254),
    password VARCHAR(128),
    confirm_password VARCHAR(128),
    key VARCHAR(128),
    terms_accepted BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES auth_user(id)
);
