import pandas as pd
import numpy as np

IrisDataFrame = pd.read_csv('iris.data', header=None, index_col=None)
print(type(IrisDataFrame))
# Convertimos el "DataFrame" a un "Numpy Array"
IrisNumpyArray = IrisDataFrame.to_numpy()
num_filas, num_columnas = IrisNumpyArray.shape
print('Num. filas = {}, Num. columnas = {}'.format(num_filas, num_columnas))
i=0
for row in IrisNumpyArray:
    i += 1
    print(i, row)
#Imprimir la primera columna del conjunto de datos
print('Columna [0]')
print(IrisNumpyArray[:, 0])
#Calcular el imprimir el promedio de la primera columna del conjunto de datos.
promedio_col_0 = np.mean(IrisNumpyArray[:, 0])
print('Promedio (Columna [0])={}'.format(promedio_col_0))