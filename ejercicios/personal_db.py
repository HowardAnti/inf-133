import sqlite3

conn = sqlite3.connect("personal_db.db")

try:
    conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
        );
        """
    )
except sqlite3.OperationalError:
    print("La tabla departamentos ya existe")


try:
    conn.execute(
        """
        CREATE TABLE CARGOS
        (id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL);
        """
    )
except sqlite3.OperationalError:
    print("La tabla cargos ya fue creada")


try:
    conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (id INTEGER PRIMARY KEY,
        nombres TEXT NOT NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        departamento_id INTEGER NOT NULL,
        cargo_id INTEGER NOT NULL,
        fecha_creacion TEXT NOT NULL,  
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La table empleados ya fue creada")


try:
    conn.execute(
        """
        CREATE TABLE SALARIOS
        (id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id));
        """
    )
except sqlite3.OperationalError:
    print("La tabla salarios ya fue creada creada")

conn.commit()
conn.close()
