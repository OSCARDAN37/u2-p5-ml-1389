import numpy as np
import pandas as pd
# Oscar Flores NC = 1389
# datos matriz 4 x 3
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas
# y almacenar la tabla en la variable df dataframe
print("--- Datos a traves de una mariz 4x3 ---")
df=pd.DataFrame(datos_alumno, columns=['ci','marcas','paquete'])
print(df)
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
# datos a partir de un diccionario
print("--- Datos a partir de un diccionario ---")
alumno_diccionario = {
'nombre':["Oscar","Juan","Joel","Andres","Azul","Axel"],
'califa':[80,90,100,80,70,50],
'edad':[16,15,16,16,18,14],
}
estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)
print("Oscar Flores NC = 1389")
