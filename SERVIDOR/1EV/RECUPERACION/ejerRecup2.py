#!C:\Users\zx22student3329\AppData\Local\Programs\Python\Python311\python.exe

#para mostrar la pagina en html

print("Content-type:text/plain\n")

#funcion que se le pasan tres parametros para usarlos en los calculos
def calcular_precio_final(precio_base, tipo_cliente, ubicacion):
    #primer bucle if para el parametro 2
    if tipo_cliente == "estudiante":
        #calculamos el desceunto que se le hace al precio si el tipo_cliente es estudiante
        descuento = precio_base*0.1
        #segundo bucle que si la ubicacion es fuera, ademas se le aplica un recargo del 5%
        if ubicacion == "fuera":
            recargo = precio_base*0.05
            precioFinal = (precio_base-descuento)+recargo
            #devolvemos el precio final
            return precioFinal
        
    #primer bucle if para el parametro 2
    if tipo_cliente == "miembro":
        #calculamos el descuento que se le hace al precio si el tipo_cliente es miembro
        descuento = precio_base*0.15
        #segundo bucle que si la ubicacion es fuera, ademas se le aplica un recargo del 5%
        if ubicacion == "fuera":
            recargo = precio_base*0.05
            precioFinal = (precio_base-descuento)+recargo
            #devolvemos el precio final
            return precioFinal

#imprimos la funcion con los valores para comprobar
print(calcular_precio_final(100, "estudiante", "fuera"))#devuelve 95.0
print(calcular_precio_final(100, "miembro", "fuera"))#devuelve 90.0

        
