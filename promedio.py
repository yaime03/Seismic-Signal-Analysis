import numpy as np
def promedio_2d(matrix, mode):
#Promedio Total
    if mode == 0:
        counter = 0
        sum = 0
        for fila in matrix:
            for value in fila:
                counter = counter + 1
                sum = sum + value
                promedio = sum / counter
# Promedio Fila
    elif mode == 1:
        promedio = np.zeros(len(matrix))
        for k in range(len(matrix)):
            sumfila = 0
            counter = 0
            for i in range(len(matrix[0])):
                sumfila = sumfila + matrix[k][i]
                counter = counter + 1
                promedio[k] = sumfila / counter
# Promedio Columna
    elif mode == 2:
        promedio = np.zeros(len(matrix[0]))
        for k in range(len(matrix[0])):
            sumcolumna = 0
            for i in range(len(matrix)):
                sumcolumna = sumcolumna + matrix[i][k]
            promedio[k] = (sumcolumna / len(matrix))
    else:
        promedio = 'No esta dentro de las opciones'

    return promedio