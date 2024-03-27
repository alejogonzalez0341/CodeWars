def better_than_average(class_points, your_points):
    # Forma manual 

    # Le asignamos el valor de la suma de la lista a la variable "suma"

    # El atributo "sum" es originario de Python 
    suma= sum(class_points)

    # Después de haber hecho la suma la dividimos por el número de estudiantes 
    divicion= suma/ len(class_points)

    # Agregamos la condición la cual verifica si mi puntaje es menor que los de los demás estudiantes, si se cumple, devolverá un "False"
    if your_points < divicion:
        return False
    
    # De lo contrario devolverá un "True"
    return True

    # Forma simplificada de hacerlo obteniendo el mismo resultado

    """

    return sum(class_points) < your_points * len(class_points)

    """
