import sqlite3

conn = sqlite3.connect(personal_db.db)

conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
    VALUES ("Ventas", "10-04-2020")
    """
)

conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion)
    VALUES ("Marketing", "11-04-2020")
    """
)

conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
    VALUES ("Gerente de Ventas","Senior", "10-04-2020")
    """
)

