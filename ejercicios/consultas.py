import sqlite3

conn = sqlite3.connect("personal_db.db")

conn.execute(
    """
    DELETE FROM SALARIOS
    """
)

conn.execute(
    """
    DELETE FROM EMPLEADOS
    """
)

conn.execute(
    """
    DELETE FROM CARGOS
    """
)

conn.execute(
    """
    DELETE FROM DEPARTAMENTOS
    """
)

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


cargos=[
    ("Gerente de Ventas", "Senior", "10-04-2020"),
    ("Analista de Marketing", "Junior", "11-04-2020"),
    ("Representante de Ventas", "Junior", "12-04-2020"),
]

sql = """
INSERT INTO CARGOS (nombre, nivel, fecha_creacion)
VALUES (?,?,?)
"""

empleados = [
    ("Juan", "Gonzalez", "Perez", "15-05-2023", 1, 1, "15-05-2023"),
    ("Maria", "Lopez", "Martinez", "20-06-2023", 2, 2, "20-06-2023"),
]

sql1 = """
INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion)
VALUES (?,?,?,?,?,?,?)
"""

salarios = [
    (1, 3000, '2024-04-01', '2025-04-30', '04-04-2024'),
    (2, 3500, '2023-07-01', '2024-04-30', '04-04-2024'),
]

sql2 = """
INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion)
VALUES (?,?,?,?,?)
"""

conn.executemany(sql, cargos)
conn.executemany(sql1, empleados)
conn.executemany(sql2, salarios)

cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, SALARIOS.salario
    FROM SALARIOS
    JOIN EMPLEADOS ON SALARIOS.empleado_id = EMPLEADOS.id
    """
)

for row in cursor:
    print(row)


cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, DEPARTAMENTOS.nombre, CARGOS.nombre
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id
    """
)

for row in cursor:
    print(row)

cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, DEPARTAMENTOS.nombre, CARGOS.nombre, SALARIOS.salario
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id
    JOIN SALARIOS ON EMPLEADOS.id = SALARIOS.empleado_id
    """
)

for row in cursor:
    print(row)


conn.execute(
    """
    UPDATE EMPLEADOS
    SET cargo_id = 3
    WHERE id = 2
    """
)

conn.execute(
    """
    UPDATE SALARIOS
    SET salario = 3600
    WHERE id = 2
    """
)

conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)


conn.execute(
    """
    DELETE FROM SALARIOS
    WHERE id = 2
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS (nombres, apellido_materno, apellido_paterno, fecha_contratacion, departamento_id, cargo_id, fecha_creacion)
    VALUES ("Carlos", "Sanchez", "Rodriguez", "09-04-2024", 1, 3, "04-04-2024")
    """
)

conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion)
    VALUES (2, 3500, "2023-05-05", "2024-12-05", "04-04-2024")
    """
)

cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, DEPARTAMENTOS.nombre, CARGOS.nombre, SALARIOS.salario
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamento_id = DEPARTAMENTOS.id
    JOIN CARGOS ON EMPLEADOS.cargo_id = CARGOS.id
    JOIN SALARIOS ON EMPLEADOS.id = SALARIOS.empleado_id
    """
)


for row in cursor:
    print(row)

conn.commit()
conn.close()