-- setup commands for sql db
-- cat sql_setup.sql | mysql -hlocalhost -uroot -p

-- CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
-- GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
-- CREATE DATABASE IF NOT EXISTS tyrell_corp;
-- USE tyrell_corp;
-- CREATE TABLE IF NOT EXISTS nexus6 (id INT, name VARCHAR(256));
-- INSERT INTO nexus6 (id, name) VALUES (1, 'Pixel');
-- GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
-- CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY '1234';
-- GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
-- GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';


CHANGE MASTER TO
    MASTER_HOST='54.234.160.185',
    MASTER_USER='replica_user',
    MASTER_PASSWORD='1234',
    MASTER_LOG_FILE='mysql-bin.000001',
    MASTER_LOG_POS=306;