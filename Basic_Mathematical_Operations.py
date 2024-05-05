def nums(operador, valor_1, valor_2):
    #concatenamos los parametros en orden de la operación y con la funcion de eval se encarga de generar la operación
    return eval(f"{valor_1}{operador}{valor_2}")





print(nums("*", 10, 10))