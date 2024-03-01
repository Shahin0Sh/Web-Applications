-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema ko_converter_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ko_converter_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ko_converter_db` DEFAULT CHARACTER SET latin1 ;
USE `ko_converter_db` ;

-- -----------------------------------------------------
-- Table `ko_converter_db`.`kc`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ko_converter_db`.`kc` (
  `kc_id` INT(11) NOT NULL AUTO_INCREMENT,
  `amount` INT(11) NOT NULL,
  `price_tr` FLOAT NOT NULL,
  `price_bgn` FLOAT NOT NULL,
  PRIMARY KEY (`kc_id`),
  UNIQUE INDEX `kc_id_UNIQUE` (`kc_id` ASC) VISIBLE,
  UNIQUE INDEX `amount_UNIQUE` (`amount` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `ko_converter_db`.`kc_ingame_price`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ko_converter_db`.`kc_ingame_price` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `kc_id` INT(11) NOT NULL,
  `ingame_price` FLOAT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_kc_ingame_price_kc1_idx` (`kc_id` ASC) VISIBLE,
  CONSTRAINT `fk_kc_ingame_price_kc1`
    FOREIGN KEY (`kc_id`)
    REFERENCES `ko_converter_db`.`kc` (`kc_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
