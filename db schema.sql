create database googlenotes;


CREATE TABLE `googlenotes`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `password` VARCHAR(50) NOT NULL,
  `created_at` DATE NOT NULL ,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
DEFAULT CHARACTER SET = utf8;


CREATE TABLE `googlenotes`.`notes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(50) NOT NULL,
  `description` TEXT NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATE NOT NULL ,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  FOREIGN KEY (`user_id`) REFERENCES `googlenotes`.`users` (`id`),
    )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE `googlenotes`.`category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `created_at` DATE NOT NULL ,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB;


CREATE TABLE `googlenotes`.`notes_category` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `notes_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  `created_at` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `notes_id_idx` (`notes_id` ASC) VISIBLE,
  INDEX `catgegory_id_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `notes_id`
    FOREIGN KEY (`notes_id`)
    REFERENCES `googlenotes`.`notes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `catgegory_id`
    FOREIGN KEY (`category_id`)
    REFERENCES `googlenotes`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
DEFAULT CHARACTER SET = utf8;
