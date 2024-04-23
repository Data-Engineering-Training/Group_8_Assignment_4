
CREATE DATABASE bankData;
use bankData;

CREATE USER 'programmer'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON bankData.customer_data to 'programmer'@'localhost';

CREATE TABLE customer_data (
    customer_id varchar(25),
    first_name varchar(20),
    last_name varchar(20),
    email varchar(20),
    transaction_activity varchar(10),
    customer_preference varchar(10)
);
SET GLOBAL local_infile=1;
LOAD DATA  INFILE '/data_frame.csv/docker-entrypoint-initdb.d/data_frame.csv' INTO TABLE customer_data FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;