
PREVENT_DUPLICATION = "DROP TABLE IF EXISTS SlavesOfDarkness"

CREATE_TABLE = """
                    CREATE TABLE SlavesOfDarkness(
                                                id INT PRIMARY KEY,
                                                name CHAR(20),
                                                age INT,
                                                phone CHAR(20),
                                                addr CHAR(20)
                                                )
                """


INSERT_INTO = """
                    INSERT INTO SlavesOfDarkness VALUES(
                                                        %d,"%s",%d,"%s","%s"
                                                        )
                """

SELECT_FROM = """
                        SELECT * FROM SlavesOfDarkness
                    """

SELECT_FROM_WHERE = """
                    SELECT * FROM SlavesOfDarkness WHERE id = %d
                """

UPDATE_SET_WHERE = """
                    UPDATE SlavesOfDarkness SET name = "%s",age = %d,phone = "%s",addr = "%s" WHERE id = %d
                """

DELETE_FROM_WHERE = """
                    DELETE FROM SlavesOfDarkness WHERE id = %d
                """

DB_name = 'DataList'