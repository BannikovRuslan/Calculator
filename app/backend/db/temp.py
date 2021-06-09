engine.execute("""
    CREATE TABLE `operations`.`operationtypes` (
        `id_operationtypes` INT NOT NULL AUTOINCREMENT,
        `operationtype` VARCHAR(45) NULL,
        PRIMARY KEY (`id_operationtypes`));
""")

engine.execute("""
    CREATE TABLE `operations`.`operationsintime` (
        `idoperationsintime` INT NOT NULL AUTOINCREMENT,
        `operationtype` INT NULL,
        `time` DATE NULL,
        PRIMARY KEY (`idoperationsintime`),
        INDEX `operationtypeFK_idx` (`operationtype` ASC) VISIBLE,
        CONSTRAINT `operationtypeFK`
        FOREIGN KEY (`operationtype`)
        REFERENCES `operations`.`operationtypes` (`idoperationtypes`)
        ON DELETE RESTRICT 
        ON UPDATE RESTRICT);
""")

engine.execute("""insert into operationtypes(opeatintype) values (`сложение`)""")
engine.execute("""insert into operationtypes(opeatintype) values (`вычитание`)""")
engine.execute("""insert into operationtypes(opeatintype) values (`генерация случаного числа`)""")
