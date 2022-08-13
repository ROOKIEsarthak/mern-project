-- ----------------------------------------------------------------------------
-- MySQL Workbench Migration
-- Migrated Schemata: pump1
-- Source Schemata: pump
-- Created: Tue Sep  8 10:07:44 2020
-- Workbench Version: 8.0.21
-- ----------------------------------------------------------------------------

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------------------------------------------------------
-- Schema pump1
-- ----------------------------------------------------------------------------
DROP SCHEMA IF EXISTS `pump1` ;
CREATE SCHEMA IF NOT EXISTS `pump1` ;

-- ----------------------------------------------------------------------------
-- Table pump1.admin
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `pump1`.`admin` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `First_name` VARCHAR(100) NULL DEFAULT NULL,
  `Last_name` VARCHAR(100) NULL DEFAULT NULL,
  `Mob_no` VARCHAR(100) NULL DEFAULT NULL,
  `Address` VARCHAR(100) NULL DEFAULT NULL,
  `Sex` VARCHAR(100) NULL DEFAULT NULL,
  `Station_id` VARCHAR(100) NULL DEFAULT NULL,
  `Time` VARCHAR(100) NULL DEFAULT NULL,
  `mail` VARCHAR(100) NULL DEFAULT NULL,
  `pass` VARCHAR(100) NULL DEFAULT NULL,
  `adminId` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table pump1.collection
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `pump1`.`collection` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `total_coll` FLOAT NULL DEFAULT NULL,
  `time` VARCHAR(100) NULL DEFAULT NULL,
  `date` VARCHAR(100) NULL DEFAULT NULL,
  `Fuel_type` VARCHAR(100) NULL DEFAULT NULL,
  `Fuel_qty` VARCHAR(100) NULL DEFAULT NULL,
  `Station_id` VARCHAR(100) NULL DEFAULT NULL,
  `Vehicle_no` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 29
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table pump1.developer
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `pump1`.`developer` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `First_name` VARCHAR(100) NULL DEFAULT NULL,
  `Last_name` VARCHAR(100) NULL DEFAULT NULL,
  `Mob_no` VARCHAR(100) NULL DEFAULT NULL,
  `Address` VARCHAR(100) NULL DEFAULT NULL,
  `Sex` VARCHAR(100) NULL DEFAULT NULL,
  `Time` VARCHAR(100) NULL DEFAULT NULL,
  `mail` VARCHAR(100) NULL DEFAULT NULL,
  `devID` VARCHAR(100) NULL DEFAULT NULL,
  `pass` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table pump1.diesel
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `pump1`.`diesel` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Vehicle_no` VARCHAR(100) NULL DEFAULT NULL,
  `Damt` FLOAT NULL DEFAULT NULL,
  `Dqty` FLOAT NULL DEFAULT NULL,
  `time` VARCHAR(100) NULL DEFAULT NULL,
  `date` VARCHAR(100) NULL DEFAULT NULL,
  `collection` FLOAT NULL DEFAULT NULL,
  `Year` VARCHAR(100) NULL DEFAULT NULL,
  `Station_id` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table pump1.gas
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `pump1`.`gas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Vehicle_no` VARCHAR(100) NULL DEFAULT NULL,
  `Gamt` FLOAT NULL DEFAULT NULL,
  `Gqty` FLOAT NULL DEFAULT NULL,
  `time` VARCHAR(100) NULL DEFAULT NULL,
  `date` VARCHAR(100) NULL DEFAULT NULL,
  `collection` FLOAT NULL DEFAULT NULL,
  `Year` VARCHAR(100) NULL DEFAULT NULL,
  `Station_id` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table pump1.petrol
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `pump1`.`petrol` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Vehicle_no` VARCHAR(100) NULL DEFAULT NULL,
  `Pamt` FLOAT NULL DEFAULT NULL,
  `Pqty` FLOAT NULL DEFAULT NULL,
  `time` VARCHAR(100) NULL DEFAULT NULL,
  `date` VARCHAR(100) NULL DEFAULT NULL,
  `collection` FLOAT NULL DEFAULT NULL,
  `Year` VARCHAR(100) NULL DEFAULT NULL,
  `Station_id` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 16
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- ----------------------------------------------------------------------------
-- Table pump1.user
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `pump1`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `First_name` VARCHAR(100) NULL DEFAULT NULL,
  `Last_name` VARCHAR(100) NULL DEFAULT NULL,
  `Mob_no` VARCHAR(100) NULL DEFAULT NULL,
  `Address` VARCHAR(100) NULL DEFAULT NULL,
  `sex` VARCHAR(100) NULL DEFAULT NULL,
  `Aadhar_no` VARCHAR(100) NULL DEFAULT NULL,
  `Vehicles` VARCHAR(100) NULL DEFAULT NULL,
  `Time` VARCHAR(100) NULL DEFAULT NULL,
  `Mail` VARCHAR(100) NULL DEFAULT NULL,
  `pass` VARCHAR(100) NULL DEFAULT NULL,
  `userid` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;
SET FOREIGN_KEY_CHECKS = 1;
