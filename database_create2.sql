-- MySQL Script generated by MySQL Workbench
-- 01/16/16 15:42:29
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Ksiazka`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Ksiazka` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Ksiazka` (
  `idKsiazka` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `autor` VARCHAR(45) NOT NULL COMMENT '',
  `tytul` VARCHAR(45) NOT NULL COMMENT '',
  `cena` FLOAT NOT NULL COMMENT '',
  `dict_img` VARCHAR(120) NOT NULL COMMENT '',
  `kategoria` VARCHAR(45) NOT NULL COMMENT '',
  PRIMARY KEY (`idKsiazka`)  COMMENT '',
  UNIQUE INDEX `idKsiazka_UNIQUE` (`idKsiazka` ASC)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Uzytkownik`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Uzytkownik` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Uzytkownik` (
  `idUzytkownik` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `login` VARCHAR(45) NOT NULL COMMENT '',
  `haslo` VARCHAR(256) NOT NULL COMMENT '',
  `adres` VARCHAR(45) NOT NULL COMMENT '',
  `nr_telefonu` INT(16) NULL COMMENT '',
  `email` VARCHAR(256) NOT NULL COMMENT '',
  PRIMARY KEY (`idUzytkownik`)  COMMENT '',
  UNIQUE INDEX `login_UNIQUE` (`login` ASC)  COMMENT '',
  UNIQUE INDEX `idUzytkownik_UNIQUE` (`idUzytkownik` ASC)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Koszyk`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Koszyk` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Koszyk` (
  `idKoszyk` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `idUzytkownik` INT NOT NULL COMMENT '',
  `data_realizacji` DATETIME NULL COMMENT '',
  `zmienna_ses_kosz` INT NOT NULL COMMENT '',
  `status_zamowienia` SMALLINT(6) NOT NULL DEFAULT 0 COMMENT '',
  PRIMARY KEY (`idKoszyk`)  COMMENT '',
  UNIQUE INDEX `zmienna_ses_UNIQUE` (`zmienna_ses_kosz` ASC)  COMMENT '',
  INDEX `fk_Koszyk_Uzytkownik3_idx` (`idUzytkownik` ASC)  COMMENT '',
  UNIQUE INDEX `idKoszyk_UNIQUE` (`idKoszyk` ASC)  COMMENT '',
  CONSTRAINT `fk_Koszyk_Uzytkownik3`
    FOREIGN KEY (`idUzytkownik`)
    REFERENCES `mydb`.`Uzytkownik` (`idUzytkownik`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`listaKoszyka`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`listaKoszyka` ;

CREATE TABLE IF NOT EXISTS `mydb`.`listaKoszyka` (
  `idKsiazka` INT NOT NULL COMMENT '',
  `idKoszyk` INT NOT NULL COMMENT '',
  `ilość` INT NOT NULL COMMENT '',
  INDEX `idKsiazek_idx` (`idKsiazka` ASC)  COMMENT '',
  INDEX `idKoszyka_idx` (`idKoszyk` ASC)  COMMENT '',
  PRIMARY KEY (`idKsiazka`, `idKoszyk`)  COMMENT '',
  CONSTRAINT `idKsiazek`
    FOREIGN KEY (`idKsiazka`)
    REFERENCES `mydb`.`Ksiazka` (`idKsiazka`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idKoszyka`
    FOREIGN KEY (`idKoszyk`)
    REFERENCES `mydb`.`Koszyk` (`idKoszyk`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Tag`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Tag` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Tag` (
  `id_Tag` INT NOT NULL COMMENT '',
  `nazwaTagu` VARCHAR(45) NOT NULL COMMENT '',
  PRIMARY KEY (`id_Tag`)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`listaTagu`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`listaTagu` ;

CREATE TABLE IF NOT EXISTS `mydb`.`listaTagu` (
  `id_Tag` INT NOT NULL COMMENT '',
  `idKsiazka` INT NOT NULL COMMENT '',
  INDEX `fk_listaTagu_Tag1_idx` (`id_Tag` ASC)  COMMENT '',
  PRIMARY KEY (`id_Tag`, `idKsiazka`)  COMMENT '',
  INDEX `fk_listaTagu_Ksiazka1_idx` (`idKsiazka` ASC)  COMMENT '',
  CONSTRAINT `fk_listaTagu_Tag1`
    FOREIGN KEY (`id_Tag`)
    REFERENCES `mydb`.`Tag` (`id_Tag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_listaTagu_Ksiazka1`
    FOREIGN KEY (`idKsiazka`)
    REFERENCES `mydb`.`Ksiazka` (`idKsiazka`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
