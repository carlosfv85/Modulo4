from clases import Vehiculo, Automovil, AutoCarga, AutoParticular, Bicicleta, Motocicleta
           
#Contenido Parte 2 de la prueba de consolidación. 
#Creación de instancias especificadas en Prueba de consolidación
particular = AutoParticular("Ford", "Fiesta", 4, "180", "500", 5)
carga = AutoCarga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Carrera", 21, "DobleViga", "2T")




#Impresión de instancias según formato especificado.
print("\nLas instancias creadas son las siguientes: ")
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

#Verificación de la relación que existe entre la instancia motocicleta con las demas clases.
print("\nLa relacion de las intancias motocicletas con las demas clases son: ")
print (f"motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}") 
print (f"motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}") 
print (f"motocicleta es instancia con relación a AutoParticular: {isinstance(motocicleta, AutoParticular)}") 
print (f"motocicleta es instancia con relación a AutoCarga: {isinstance(motocicleta, AutoCarga)}")
print (f"motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}") 
print (f"motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}") 







  


