def cadena(texto)-> str:
    # creamos una variable vacia como tipo texto
    nuevo_texto = ""
    # tenemos las vocales minuculas y mayuculas en una variable
    vocales = "aeiou"
    #generamos un ciclo for para que recorra cada elemento de el parametro string
    for letra in texto:
        #validamos si la letra del siclo for no esta en la variable vocales 
        if letra not in vocales:
            #llamamos a la variable nuevo_texto y le agregamos cada letra la cual no esta el la validacion 
            nuevo_texto += letra
    # devolvemos el valor de nuevo_texto
    return nuevo_texto            
