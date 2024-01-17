--  Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE `states` IF NOT EXISTS `states` (`id` INT NOT NULL, `name` VARCHAR(256) NOT NULL, CONSTRAINT states_pk PRIMARY kEY(`id`), UNIQUE key id_unique (id));
