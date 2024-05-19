def number_square(lista_numeros: int):
    # creamos una lista vacia 
    lista_vacia= []
    # pasamos la lista de numeros a cadena de texto
    numeros_a_texto= str(lista_numeros)
    # generamos un for para que recorra cada elemento de la lista 
    for i in numeros_a_texto:
        #tipamos nuevamente de cadena de texto a numero la variable y le asignamos la raiz cuadrada a cada numero de la lista
        retultado=int(i)**2
        # le asignamos el valor de resultado a la variable de la lista vacia
        lista_vacia.append(retultado)
    # tipamos nuevamente a cadena de texto la variable unificamos  cada elemento de la lista vacia le quitamos las comas ejemplo [4, 16, 4, 25] pasa a [416425]
    test= "".join(map(str, lista_vacia))
    #devolvemos al tipo de variable a numero
    int_test= int(test)
    #devolvemos el valor
    return int_test
