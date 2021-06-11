import os
from os import listdir
from os.path import isfile, join
from shutil import copyfile
import random
carpeta_origen_gatos = os.path.join(".", "Bases de datos\\PERROS Y GATOS\\training_set\\training_set\\cats")
carpeta_origen_perros = os.path.join(".", "Bases de datos\\PERROS Y GATOS\\training_set\\training_set\\dogs")
carpeta_origen_gatos_test = os.path.join(".", "Bases de datos\\PERROS Y GATOS\\test_set\\test_set\\cats")
carpeta_origen_perros_test = os.path.join(".", "Bases de datos\\PERROS Y GATOS\\test_set\\test_set\\dogs")



origen_gatos = [f for f in listdir(carpeta_origen_gatos) if isfile(join(carpeta_origen_gatos, f))]
origen_perros = [f for f in listdir(carpeta_origen_perros) if isfile(join(carpeta_origen_perros, f))]
origen_gatos_test = [f for f in listdir(carpeta_origen_gatos_test) if isfile(join(carpeta_origen_gatos_test, f))]
origen_perros_test = [f for f in listdir(carpeta_origen_perros_test) if isfile(join(carpeta_origen_perros_test, f))]

entrenamiento=300
validacion=100
prueba=100



g_ev=random.sample(range(len(origen_gatos)), entrenamiento+validacion)
g_p=random.sample(range(len(origen_gatos_test)), prueba)

p_ev=random.sample(range(len(origen_perros)), entrenamiento+validacion)
p_p=random.sample(range(len(origen_perros_test)), prueba)


for i in range(entrenamiento):
    src=carpeta_origen_gatos+"\\"+str(origen_gatos[g_ev[i]])
    dst=".\\Gatos_Entrenamiento\\"+"Gato."+str("%03d" % (i+1,))+".jpg"
    print(dst)
    copyfile(src, dst)
    
for j in range(validacion):
    src=carpeta_origen_gatos+"\\"+str(origen_gatos[g_ev[j+entrenamiento]])
    dst=".\\Gatos_Validacion\\"+"Gato."+str("%03d" % (j+1,))+".jpg"
    print(dst)
    copyfile(src, dst)

for k in range(prueba):
    src=carpeta_origen_gatos_test+"\\"+str(origen_gatos_test[g_p[k]])
    dst=".\\Gatos_Test\\"+"Gato."+str("%03d" % (k+1,))+".jpg"
    print(dst)
    copyfile(src, dst)
    
for i in range(entrenamiento):
    src=carpeta_origen_perros+"\\"+str(origen_perros[p_ev[i]])
    dst=".\\Perros_Entrenamiento\\"+"Perro."+str("%03d" % (i+1,))+".jpg"
    print(dst)
    copyfile(src, dst)
    
for j in range(validacion):
    src=carpeta_origen_perros+"\\"+str(origen_perros[p_ev[j+entrenamiento]])
    dst=".\\Perros_Validacion\\"+"Perro."+str("%03d" % (j+1,))+".jpg"
    print(dst)
    copyfile(src, dst)

for k in range(prueba):
    src=carpeta_origen_perros_test+"\\"+str(origen_perros_test[p_p[k]])
    dst=".\\Perros_Test\\"+"Perro."+str("%03d" % (k+1,))+".jpg"
    print(dst)
    copyfile(src, dst)