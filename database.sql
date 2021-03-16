DROP DATABASE IF EXISTS trojboj_baza;

CREATE DATABASE trojboj_baza;

USE trojboj_baza;

CREATE TABLE `user` (
    `id` int(10) NOT NULL AUTO_INCREMENT,
    `login` varchar(50) NOT NULL UNIQUE,
    `password` varchar(50) NOT NULL,
    `imie` varchar(50) NOT NULL UNIQUE,
    `nazwisko` varchar(50) NOT NULL,
    `wzrost` int(5) NOT NULL,
    PRIMARY KEY(id)
    ) Engine=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `weight` (
	`id` int(10) NOT NULL AUTO_INCREMENT,
	`idUser` int(10) NOT NULL,
	`weight` int(5) NOT NULL,
	`date` date NOT NULL UNIQUE,
	PRIMARY KEY(id),
	KEY `FK_IdUser` (`idUser`)
	) Engine=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `results` (
	`id` int(10) NOT NULL AUTO_INCREMENT,
	`idUser` int(10) NOT NULL,
	`date` date NOT NULL UNIQUE,
	`squat` int(5),
	`bench_press` int(5),
	`deadlift` int(5),
	PRIMARY KEY(id),
	KEY `FK_IdUser_2` (`idUser`)
	) Engine=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `weight`
	ADD CONSTRAINT `FK_IdUser` FOREIGN KEY (`idUser`) REFERENCES `user` (`id`);
ALTER TABLE `results`
	ADD CONSTRAINT `FK_IdUser_2` FOREIGN KEY (`idUser`) REFERENCES `user` (`id`);

INSERT INTO `user` VALUE (NULL,"login","password","imie","nazwisko",1);