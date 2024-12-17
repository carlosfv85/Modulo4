from clases import Vehiculo, Automovil, AutoCarga, AutoParticular, Bicicleta, Motocicleta

#Contenido Parte 3 de la prueba de consolidación. 

#Creación de instancias para posterior guardado.
#Estas instancias se guardaran con el metodo guardar_datos_csv de la clase Vehiculos como clase padre de las instancias creadas.            
particular = AutoParticular("Ford", "Fiesta", 4, "180", "500", 5)
carga = AutoCarga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Carrera", 21, "DobleViga", "2T")


lista_vehiculos = [particular, carga, bicicleta, motocicleta]

#Se guardan las instancias en el archivo (vehiculos.csv (especificado dentro de Clase Vehiculo)
Vehiculo.guardar_datos_csv(lista_vehiculos)

#Se imprime la información contenida en el archivo para la clase Vehiculo.
Vehiculo.leer_datos_csv()