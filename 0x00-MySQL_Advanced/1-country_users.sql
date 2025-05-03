-- Script that creates a table users with:
-- id: integer, never null, auto increment, primary key
-- email: string (255 chars), never null, unique
-- name: string (255 chars)
-- country: enumeration of countries (US, CO, TN), never null, default = US

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);
