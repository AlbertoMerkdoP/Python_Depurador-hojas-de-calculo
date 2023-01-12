import pandas as pd
from unidecode import unidecode 

#Seleccionar el archivo de Excel
reporte = pd.read_excel("rutadearchivoexcel.xls")

#Crear DataFrame
final = pd.DataFrame(reporte)

#Funcion que elimina las comillas
def cl(s):
  return s.replace("'", "")

#Recorrer cada celda y transformar los caracteres especiales
for column in final:
  for value in final[column]:
    if type(value) == str:
      final[column] = final[column].replace(value,unidecode(value))
      final[column] = final[column].replace(value, cl(value))

#Exportar a CSV
final.to_csv("nombrefinal.csv",index=False, decimal=",")
