#Función inicial resive 2 parametros
#x = al numero por el cual multiplicar
#n = al numero de veces el cual se debe multiplicar
def count_by(x, n):

    #Forma manual

    #Hacemos un for junto con un range el cual inicia desde el numero 1 y termina el recorrido hasta n veces 
    #y le agregamos +1 para que me tome en cuenta el ultimo numero
    for i in range(1, n+1):

        #imprimimos la variable i y lo multiplicamos por x el cual nos multiplica el i por el por la cantidad de x cada que pase un recorrido
        print(i* x)

    #Forma simplificada obteniendo el mismo resultado
    """
    return [i*x for i in range(1, n+1)]
    """

if __name__=="__main__":
    count_by(x=100, n=5)