## menu que nunca cierre el proceso se hace con while

## primero se crea un contador, variable.  y se le asigna valor

contador=0
print("Enamorate de antioquia")
print("Menu")
print("1. Agregar pueblos")
print("2. Mostras rutas ")
print("3. Salir  ")
pueblos=[]
while (contador!=3):
    pueblo={}
    contador=int (input ("Digite una opcion"))
    if (contador==1):
        print("Agregando pueblo:")
        pueblo['nombre']= input("Ingrese un nombre del pueblo")
        pueblo['distancia']=int(input("ingrese la distancia de los pueblos"))
        pueblo['poblacion']=int(input("ingrese el numero de personas en el pueblo"))
        pueblo.append(pueblo)
    elif(contador==2):
            print("mostrando rutas")
            print(pueblos)
    elif(contador==3):
            print("Saliendo")
            break
    else:
            print("opcion invalida")    
    
        