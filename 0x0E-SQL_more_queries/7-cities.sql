--  creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `cities` (`id` INT NOT NULL, `state_id` INT NOT NULL, `name` VARCHAR(256) NOT NULL, CONSTRAINT cities_pk PRIMARY KEY (`id`), UNIQUE KEY id_unique (`id`));
ALTER TABLE cities ADD CONSTRAINT cities_FK (`state_id`) REFERENCES `states` (`id`);
