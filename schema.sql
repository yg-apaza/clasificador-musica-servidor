-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema clasificador
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema clasificador
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `clasificador` ;
USE `clasificador` ;

-- -----------------------------------------------------
-- Table `clasificador`.`songs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clasificador`.`songs` (
  `id` INT ZEROFILL NOT NULL AUTO_INCREMENT,
  `filename` VARCHAR(255) NULL,
  `genre` INT NULL,
  `data` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
