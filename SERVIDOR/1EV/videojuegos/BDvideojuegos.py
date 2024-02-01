import mysql.connector, sys

#####################################################
##################LO DE API ES PARA CLIENTE###############################
#BORRAR TABLA-> DROP TABLE nombreTabla

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

        #actualizamos la tabla haciendo un commit IMPORTANTE
        self.bdconex.commit()

        miCursor.close()

    def insertar(self,nombre,empresa,tematica,numJug,anio):
        miCursor = self.bdconex.cursor()
        #crear consulta
        #OTRA FORMA DE HACER CONSULTAS
        consulta = "INSERT INTO videojuegosantiguos (nombre, empresa, tematica, numero_de_jugadores, publicacion) VALUES (%s, %s, %s, %s, %s)" 
        val=(nombre,empresa,tematica,numJug,anio)
        #se escribe en error.log y lo usamos para saber si la consulta se esta ejecutando bien
        sys.stderr.write("======================"+consulta+"======================")
        #ejecutamos la consulta
        miCursor.execute(consulta,val) #EXECUTEMANY -> SI VAMOS A AÑADIR UNA LISTA DE TUPLAS POR EJEMPLO
        ###################################

        #actualizamos la tabla haciendo un commit IMPORTANTE
        self.bdconex.commit()
        #cerrar cursos y conector
        miCursor.close()

    def modificar(self, id,nombre,empresa,tematica,numJug,anio):
        miCursor = self.bdconex.cursor()
        #crear consulta
        #OTRA FORMA DE HACER CONSULTAS
        consulta = "UPDATE videojuegosantiguos SET nombre=%s,empresa=%s,tematica=%s,numero_de_jugadores=%s,publicacion=%s WHERE id=%s" 
        val=(nombre,empresa,tematica,int(numJug),int(anio),int(id))
        #se escribe en error.log y lo usamos para saber si la consulta se esta ejecutando bien
        sys.stderr.write("======================"+consulta+"======================")
        #ejecutamos la consulta
        miCursor.execute(consulta,val) #EXECUTEMANY -> SI VAMOS A AÑADIR UNA LISTA DE TUPLAS POR EJEMPLO
        ###################################


        #actualizamos la tabla haciendo un commit IMPORTANTE
        self.bdconex.commit()
        #cerrar cursos y conector
        miCursor.close()

    def seleccionarPorId(self, id):
        miCursor = self.bdconex.cursor()
        #crear consulta
        consulta = "SELECT * FROM  videojuegosantiguos WHERE id = " + id 
        #se escribe en error.log y lo usamos para saber si la consulta se esta ejecutando bien
        sys.stderr.write("======================"+consulta+"======================")
        #ejecutamos la consulta
        miCursor.execute(consulta) 

        #recuperar la tupla con los datos buscados por el id
        miresultado = miCursor.fetchone() #trae una fila

        #cerrar cursos y conector
        miCursor.close()

        return miresultado

    def cerrarBD(self):
        self.bdconex.close()
