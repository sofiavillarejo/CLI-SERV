#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

#para mostrar la pagina en html
print("Content-type: text/html\n")

#lista de tuplas con los datos
redes_sociales=[("Twitter", "https://twitter.com/ejemplo_usuario"),
("Facebook","https://facebook.com/ejemplo_usuario"),
("Instagram","https://instagram.com/ejemplo_usuario"),
("LinkedIn","https://linkedin.com/in/ejemplo_usuario"),
("YouTube","https://youtube.com/c/ejemplo_usuario")]

#contador para generar los id
cont=1
#bucle for que recorre los datos de la lista
for red in redes_sociales:
    #formateo para imprimir el primer dato de la lista con un enlace y con cada id propio
    print(f"<ul><li id='red{cont}'><a href='{red[1]}'>" +str(red[0])+ "</a></li></ul>")
    #incrementar el contador para cada id hasta que llegue al ultimo dato
    cont+=1
    

