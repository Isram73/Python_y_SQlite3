import sqlite3

conexion = sqlite3.connect('Ejemplo.db')

c = conexion.cursor()

#c.execute("CREATE TABLE acciones (fecha text, operacion text, simbolo text, calidad real, precio real)")

c.execute("INSERT INTO acciones VALUES ('21/NOV/2016', 'compra', 'INV', '100', '15.43')")
c.execute("INSERT INTO acciones VALUES ('22/NOV/2016', 'compra', 'INV', '100', '15.43')")
c.execute("INSERT INTO acciones VALUES ('23/NOV/2016', 'compra', 'INV', '100', '15.43')")
c.execute("INSERT INTO acciones VALUES ('24/NOV/2016', 'compra', 'INV', '100', '15.43')")
c.execute("INSERT INTO acciones VALUES ('25/NOV/2016', 'compra', 'INV', '100', '15.43')")

#c.execute("SELECT * FROM acciones")

conexion.commit()

conexion.close()