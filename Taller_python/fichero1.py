import os 
import pathlib
"""file = open("Archivo1.txt", "w" )#sirve para crear un archivo) 
"""
#punto 1
"""nombre=input("Ingrese el nobre del fichero")
if os.path.isfile(nombre)== True:
    os.rename(nombre,"Archivo1.txt")
else:
    print("El fichero no existe")"""
  #punto 2  
"""nombre=input("Ingrese el nobre del fichero")
if os.path.isfile(nombre)== True:
    os.remove("Archivo2.txt")
else:
    print("el fichero no existe")"""
    
    #punto 3
"""with open("Archivo3.txt","r") as readfile:
    lineas = readfile.readline()
    nombre = []
    edad = []
    sexo=[]
    fecha_nacimiento=[]
    estatura=[]
    for c_linea in readfile:
        renglon=c_linea.split(",")
        nombre.append(renglon[0])
        edad.append(renglon[1])
        sexo.append(renglon[2])
        fecha_nacimiento.append(renglon[3])
        estatura.append(renglon[4])
print(nombre)
print(edad)
print(sexo)
print(fecha_nacimiento)
print(estatura)"""

#punto 4
with open("Archivo4.txt","r") as readfile:
    lineas = readfile.readline()
    departamentos = []
    capitales = []
    for c_linea in readfile:
        renglon=c_linea.split(":")
        departamentos.append(renglon[0])
        capitales.append(renglon[1])
print(departamentos)
print(capitales)