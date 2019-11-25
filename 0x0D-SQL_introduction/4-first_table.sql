--  script that creates a table called first_table in the current database in your MySQL server
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS first_table (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256));
