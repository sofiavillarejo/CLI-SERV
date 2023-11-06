import mysql.connector, sys

#clase que implementa las operaciones con la base de datos
class BDVideojuegos:
    #contructor del objeto para conectar con la base de datos
    def __init__(self):
        self.bdconex = mysql.connector.connect( 
            host = "localhost",
            user = "videojuegos",
            password = "videojuegos",
            database = "videojuegos"
        )

    #fin de constructor

    def todosLosVideojuegos(self):
        #cursos para hacer peticiones -> objeto que permite hacer consultas a la BBDD
        miCursor = self.bdconex.cursor()
        #crear consulta
        consulta = "SELECT * FROM videojuegosantiguos ORDER BY nombre ASC" #seleccionamos todos los campos de la tabla datos

        #ejecutamos la consulta
        miCursor.execute(consulta) 

        #devuelve todas las filas que haya en la tabla y se guardan en la variable
        miResultado = miCursor.fetchall() 
        #traza para ver el objeto miResultado
        sys.stderr.write(str(miResultado)+"\n") #devuelve una lista de tuplass

        #cerrar cursos y conector
        miCursor.close()

        #devolver los datos
        return miResultado
    
    def juegosConFiltro(self, filtro):
        #cursos para hacer peticiones -> objeto que permite hacer consultas a la BBDD
        miCursor = self.bdconex.cursor()
        #crear consulta
        consulta = "SELECT * FROM videojuegosantiguos "+ filtro + " ORDER BY nombre" #seleccionamos todos los campos de la tabla datos
        sys.stderr.write(str(consulta))
        #ejecutamos la consulta
        miCursor.execute(consulta) 

        #devuelve todas las filas que haya en la tabla y se guardan en la variable
        miResultado = miCursor.fetchall() 
        #traza para ver el objeto miResultado
        sys.stderr.write(str(miResultado)+"\n") #devuelve una lista de tuplass

        #cerrar cursos y conector
        miCursor.close()

        #devolver los datos
        return miResultado
    def borrarPorId(self,id):
        miCursor = self.bdconex.cursor()
        #crear consulta
        consulta = "DELETE FROM videojuegosantiguos WHERE id= " + id #seleccionamos todos los campos de la tabla datos
        #se escribe en error.log y lo usamos para saber si la consulta se esta ejecutando bien
        sys.stderr.write("======================"+consulta+"======================")
        #ejecutamos la consulta
        miCursor.execute(consulta)

        #actualizamos la tabla haciendo un commit
        self.bdconex.commit()

        miCursor.close()

    def cerrarBD(self):
        self.bdconex.close()
