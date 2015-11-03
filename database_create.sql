-- MySQL Script generated by MySQL Workbench
-- 10/29/15 18:47:08
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema tas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tas` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `tas` ;

-- -----------------------------------------------------
-- Table `tas`.`Ksiazka`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tas`.`Ksiazka` ;

CREATE TABLE IF NOT EXISTS `tas`.`Ksiazka` (
  `idKsiazka` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `autor` VARCHAR(45) NOT NULL COMMENT '',
  `tytul` VARCHAR(45) NOT NULL COMMENT '',
  `cena` FLOAT NOT NULL COMMENT '',
  `dict_img` VARCHAR(120) NOT NULL COMMENT '',
  `kategoria` VARCHAR(45) NOT NULL COMMENT '',
  PRIMARY KEY (`idKsiazka`)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tas`.`listaKoszyka`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tas`.`listaKoszyka` ;

CREATE TABLE IF NOT EXISTS `tas`.`listaKoszyka` (
  `idlistaKoszyka` INT NOT NULL COMMENT '',
  `idKsiazek` INT NOT NULL COMMENT '',
  `idKoszyka` INT NOT NULL COMMENT '',
  PRIMARY KEY (`idlistaKoszyka`)  COMMENT '',
  INDEX `idKsiazek_idx` (`idKsiazek` ASC)  COMMENT '',
  INDEX `idKoszyka_idx` (`idKoszyka` ASC)  COMMENT '',
  CONSTRAINT `idKsiazek`
    FOREIGN KEY (`idKsiazek`)
    REFERENCES `tas`.`Ksiazka` (`idKsiazka`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idKoszyka`
    FOREIGN KEY (`idKoszyka`)
    REFERENCES `tas`.`Koszyk` (`idKoszyk`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tas`.`Koszyk`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `tas`.`Koszyk` ;

CREATE TABLE IF NOT EXISTS `tas`.`Koszyk` (
  `idKoszyk` INT NOT NULL COMMENT '',
  `wart_Kosz` FLOAT NULL COMMENT '',
  `ilosc_Ksiaz` INT NULL COMMENT '',
  `id_Listy` INT NOT NULL COMMENT '',
  PRIMARY KEY (`idKoszyk`)  COMMENT '',
  INDEX `id_Listy_idx` (`id_Listy` ASC)  COMMENT '',
  CONSTRAINT `id_Listy`
    FOREIGN KEY (`id_Listy`)
    REFERENCES `tas`.`listaKoszyka` (`idlistaKoszyka`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;