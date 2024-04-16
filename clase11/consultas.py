# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("restaurante.db")

# Insertamos nuevos estudiantes y carreras

conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Pizza', 10.99, 'Italiana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Hamburguesa', 8.99, 'Americana')
    """
)

conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Sushi', 12.99, 'Japonesa')
    """)

conn.execute(
    """
    INSERT INTO PLATOS (nombre, precio, categoria) 
    VALUES ('Ensalada', 8.99, 'Vegetariana')
    """
)


conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (1)
    """
)

conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (2)
    """
)

conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero) 
    VALUES (4)
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (1, 2, 2, '2024-02-01')
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (1, 2, 3, '2024-04-01')
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (3, 3, 3, '2024-04-02')
    """
)

conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id, mesa_id, cantidad, fecha) 
    VALUES (4, 4, 1, '2024-04-02')
    """
)




cursor=conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero
    FROM PEDIDOS
    JOIN PLATOS on PEDIDOS.plato_id= PLATOS.id
    JOIN MESAS on PEDIDOS.mesa_id= MESAS.id
    """
)

for row in cursor:
    print(row)

cursor=conn.execute(
    """
    SELECT PLATOS.nombre
    FROM PEDIDOS
    LEFT JOIN PLATOS on PEDIDOS.plato_id= PLATOS.id
    """
)

for row in cursor:
    print(row)



conn.commit()
# Cerrar conexión
conn.close()