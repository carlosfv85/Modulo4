import csv

#Diagrama de clase en el archivo diagrama.drawio.png es una suma de lo solicitado en Parte 1 y 2 de la Prueba de consolidación.


#Contenido Parte 1 de la prueba de consolidación
class Vehiculo:
    
    archivo = "vehiculos" 
    formato = "csv"
    
    def __init__(self, marca:str, modelo:str, num_ruedas:int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas
        
                
    def __str__(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.num_ruedas} ruedas"
    
#Contenido Parte 3 de la Prueba de consolidación   
    @classmethod
    def guardar_datos_csv(self, vehiculo_o_lista):
        """ Guarda los datos de una instancia de vehículo o de una lista/tupla de instancias de clase en un archivo csv.
            Si el archivo no existe, lo crea; si ya existe, añade los datos al archivo sin sobreescribirlo.
            Se guarda cada instancia con su nombre de la clase y un diccionario con sus atributos.

        
        Args:
        vehiculo_o_lista : Este atributo puede ser una única instancia de clase o una lista o tupla de instancias.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "a", newline= "\n", encoding= "utf-8") as nuevo_archivo:
                writer = csv.writer(nuevo_archivo)
                
                
                
                if isinstance (vehiculo_o_lista, list) or isinstance(vehiculo_o_lista, tuple):
                    for vehiculo in vehiculo_o_lista:
                        fila = [(vehiculo.__class__, vehiculo.__dict__)]
                        writer.writerow(fila)
                else:
                    vehiculo = vehiculo_o_lista
                    fila = [(vehiculo.__class__, vehiculo.__dict__)]         
                    writer.writerow(fila)
                    
                    
        except FileNotFoundError:
            print(f"No es posible crear o guardar contenido en el archivo {self.archivo}.{self.formato} ya que no se encuentra la ruta o directorio que lo contiene.")

    
        except Exception as e:
            print("Error: ", e)
        
        
    @classmethod
    def leer_datos_csv(self):
        """Lee el archivo existente que almacena la información para la clase Vehiculos. La información contenida se clasificará según la clase a la que pertenece cada instancia y se imprimira en terminal.
           Dada su clasificación, se excluira la impresión directa sobre la propia clase para cada instancia.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "r") as nuevo_archivo:
                reader = csv.reader(nuevo_archivo)
                
            
                lista_auto = []
                lista_autoparticular = []
                lista_autocarga = []    
                lista_bici = []
                lista_moto = []
                
                    
                for fila in reader:
                    fila = str(fila)
                    if "Automovil" in fila:
                        fila = fila.rstrip(')"]')
                        lista_auto.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoParticular" in fila:
                        fila = fila.rstrip(')"]')
                        lista_autoparticular.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoCarga" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_autocarga.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Bicicleta" in (fila):
                        fila = fila.rstrip(')"]')
                        lista_bici.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Motocicleta" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_moto.append(list(fila.split(",", maxsplit = 1)))
                        
                                     
                    else: 
                        print("No se encuentra el tipo de vehiculo")
               
               #Se imprimen las listas si existen. Se excluye su clase en la impresión.
                if lista_auto:
                    print("\nLista de Vehiculos Automovil")
                    for vehiculo in lista_auto:
                        print(vehiculo [1])
                        
                if lista_autoparticular:
                    print("\nLista de Vehiculos Particular")
                    for vehiculo in lista_autoparticular:
                        print(vehiculo[1])
                          
                if lista_autocarga:
                    print("\nLista de Vehiculos Carga")
                    for vehiculo in lista_autocarga:
                        print(vehiculo[1])
                        
                if lista_bici:
                    print("\nLista de Vehiculos Bicicleta")
                    for vehiculo in lista_bici:
                        print(vehiculo[1])
                          
                if lista_autoparticular:
                    print("\nLista de Vehiculos Motocicleta")
                    for vehiculo in lista_moto:
                        print(vehiculo[1])
                          
                          
        except FileNotFoundError:
            print(f"No es posible leer el archivo {self.archivo}.{self.formato} porque no existe un archivo con este nombre")


        except Exception as e:
            print("Error: ", e)
        
        
#Contenido Parte 1 de la prueba de consolidación        
class Automovil(Vehiculo):
    
    archivo = "automovil" 
    formato = "csv"
    
    def __init__(self, marca:str, modelo:str, num_ruedas:int, velocidad:int, cilindrada:int) -> None:
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
        
    
    def __str__(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.num_ruedas} ruedas, {self.velocidad} km/h, {self.cilindrada} cc"
        
    @staticmethod
    def datos_auto():
            try:
                cant_vehiculos = int(input("Cuántos vehículos desea insertar: "))
                
            except ValueError:
                print("El número de vehículos debe ser un valor entero.")
            except Exception as e:
                print("Error: ", e)
                
            num = 1
            vehiculos_dict = {}
            lista_automovil= []   
            
           
            while num <= cant_vehiculos:
                
                try:
                    
                    print (f"Datos del automovil {num}")
                    marca = str(input(f"Inserte la marca de automovil {num}: "))
                    modelo = str(input(f"Inserte el modelo {num}: ")) 
                    num_ruedas = int(input(f"Inserte el numero de ruedad {num}: ")) 
                    velocidad = int(input(f"Inserte la velocidad en km/h {num}: "))
                    cilindrada = int(input(f"Inserte el cilindraje en cc {num}: ")) 
                        
                    auto = Automovil(marca, modelo, num_ruedas, velocidad, cilindrada)
                    vehiculos_dict[num] = auto.__str__()
                    lista_automovil.append(auto)
                    num+=1
                     
                except ValueError:
                    print("\nEl dato ingresado no corresponde al tipo de dato solicitado\nIngrese los datos nuevamente.\n")
                    continue
                
                except Exception as e:
                    print("Error: ", e)
                            

                print("\nImprimiendo por pantalla los Vehículos...") 
                for clave, valor in vehiculos_dict.items():
                        print (f"\nDatos del automovil {clave} : {valor}")    
                        
                return lista_automovil   
            
                
            
            
              
#Contenido Parte 3 de la Prueba de consolidación             
    @classmethod
    def guardar_datos_csv(self, automovil_o_lista):
        """ Guarda los datos de una instancia de vehículo o de una lista/tupla de instancias de clase en un archivo csv.
            Si el archivo no existe, lo crea; si ya existe, añade los datos al archivo sin sobreescribirlo.
            Se guarda cada instancia con su nombre de la clase y un diccionario con sus atributos.

        
        Args:
        vehiculo_o_lista : Este atributo puede ser una única instancia de clase o una lista o tupla de instancias.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "a", newline= "\n", encoding= "utf-8") as nuevo_archivo:
                writer = csv.writer(nuevo_archivo)
                            
                
                if isinstance (automovil_o_lista, list) or isinstance(automovil_o_lista, tuple):
                    for automovil in automovil_o_lista:
                        fila = [(automovil.__class__, automovil.__dict__)]
                        writer.writerow(fila)
                else:
                    vehiculo = automovil_o_lista
                    fila = [(vehiculo.__class__, vehiculo.__dict__)]         
                    writer.writerow(fila)
                    
                    
        except FileNotFoundError:
            print(f"No es posible crear o guardar contenido en el archivo {self.archivo}.{self.formato} ya que no se encuentra la ruta o directorio que lo contiene.")
    
        except Exception as e:
            print("Error: ", e)
                    
    
    @classmethod
    def leer_datos_csv(self):
        """Lee el archivo existente que almacena la información para la clase Automovil. La información contenida se clasificará según la clase a la que pertenece cada instancia y se imprimira en terminal.
           Dada su clasificación, se excluira la impresión directa sobre la propia clase para cada instancia.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "r") as nuevo_archivo:
                reader = csv.reader(nuevo_archivo)
                
            
                lista_auto = []
                lista_autoparticular = []
                lista_autocarga = []    
                lista_bici = []
                lista_moto = []
                
                    
                for fila in reader:
                    fila = str(fila)
                    if "Automovil" in fila:
                        fila = fila.rstrip(')"]')
                        lista_auto.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoParticular" in fila:
                        fila = fila.rstrip(')"]')
                        lista_autoparticular.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoCarga" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_autocarga.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Bicicleta" in (fila):
                        fila = fila.rstrip(')"]')
                        lista_bici.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Motocicleta" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_moto.append(list(fila.split(",", maxsplit = 1)))
                        
                                     
                    else: 
                        print("No se encuentra el tipo de vehiculo")
               
               #Se imprimen las listas si existen. Se excluye su clase en la impresión.
                if lista_auto:
                    print("\nLista de Vehiculos Automovil")
                    for vehiculo in lista_auto:
                        print(vehiculo [1])
                        
                if lista_autoparticular:
                    print("\nLista de Vehiculos Particular")
                    for vehiculo in lista_autoparticular:
                        print(vehiculo[1])
                          
                if lista_autocarga:
                    print("\nLista de Vehiculos Carga")
                    for vehiculo in lista_autocarga:
                        print(vehiculo[1])
                        
                if lista_bici:
                    print("\nLista de Vehiculos Bicicleta")
                    for vehiculo in lista_bici:
                        print(vehiculo[1])
                          
                if lista_autoparticular:
                    print("\nLista de Vehiculos Motocicleta")
                    for vehiculo in lista_moto:
                        print(vehiculo[1])
                          
                          
        except FileNotFoundError:
            print(f"No es posible leer el archivo {self.archivo}.{self.formato} porque no existe un archivo con este nombre")


        except Exception as e:
            print("Error: ", e)
    
        
class AutoParticular(Automovil):
    
    archivo = "autosparticulares" 
    formato = "csv"
    
    def __init__(self, marca:str, modelo:str, num_ruedas:int, velocidad:int, cilindrada:int, num_puestos:int) -> None:
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.num_puestos = num_puestos
    
    def __str__(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.num_ruedas} ruedas, {self.velocidad} km/h, {self.cilindrada} cc, Puestos: {self.num_puestos}"    

#Contenido Parte 3 de la Prueba de consolidación 
    @classmethod
    def guardar_datos_csv(self, autoparticular_o_lista):
        """ Guarda los datos de una instancia de vehículo o de una lista/tupla de instancias de clase en un archivo csv.
            Si el archivo no existe, lo crea; si ya existe, añade los datos al archivo sin sobreescribirlo.
            Se guarda cada instancia con su nombre de la clase y un diccionario con sus atributos.

        
        Args:
        vehiculo_o_lista : Este atributo puede ser una única instancia de clase o una lista o tupla de instancias.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "a", newline= "\n", encoding= "utf-8") as nuevo_archivo:
                writer = csv.writer(nuevo_archivo)
                
                
                
                if isinstance (autoparticular_o_lista, list) or isinstance(autoparticular_o_lista, tuple):
                    for autoparticular in autoparticular_o_lista:
                        fila = [(autoparticular.__class__, autoparticular.__dict__)]
                        writer.writerow(fila)
                else:
                    autoparticular = autoparticular_o_lista
                    fila = [(autoparticular.__class__, autoparticular.__dict__)]         
                    writer.writerow(fila)
                    
                    
        except FileNotFoundError:
            print(f"No es posible crear o guardar contenido en el archivo {self.archivo}.{self.formato} ya que no se encuentra la ruta o directorio que lo contiene.")
    
        except Exception as e:
            print("Error: ", e)


    @classmethod
    def leer_datos_csv(self):
        """Lee el archivo existente que almacena la información para la clase AutoParticular. La información contenida se clasificará según la clase a la que pertenece cada instancia y se imprimira en terminal.
           Dada su clasificación, se excluira la impresión directa sobre la propia clase para cada instancia.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "r") as nuevo_archivo:
                reader = csv.reader(nuevo_archivo)
                
            
                lista_auto = []
                lista_autoparticular = []
                lista_autocarga = []    
                lista_bici = []
                lista_moto = []
                
                    
                for fila in reader:
                    fila = str(fila)
                    if "Automovil" in fila:
                        fila = fila.rstrip(')"]')
                        lista_auto.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoParticular" in fila:
                        fila = fila.rstrip(')"]')
                        lista_autoparticular.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoCarga" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_autocarga.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Bicicleta" in (fila):
                        fila = fila.rstrip(')"]')
                        lista_bici.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Motocicleta" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_moto.append(list(fila.split(",", maxsplit = 1)))
                        
                                     
                    else: 
                        print("No se encuentra el tipo de vehiculo")
               
               #Se imprimen las listas si existen. Se excluye su clase en la impresión.
                if lista_auto:
                    print("\nLista de Vehiculos Automovil")
                    for vehiculo in lista_auto:
                        print(vehiculo [1])
                        
                if lista_autoparticular:
                    print("\nLista de Vehiculos Particular")
                    for vehiculo in lista_autoparticular:
                        print(vehiculo[1])
                          
                if lista_autocarga:
                    print("\nLista de Vehiculos Carga")
                    for vehiculo in lista_autocarga:
                        print(vehiculo[1])
                        
                if lista_bici:
                    print("\nLista de Vehiculos Bicicleta")
                    for vehiculo in lista_bici:
                        print(vehiculo[1])
                          
                if lista_autoparticular:
                    print("\nLista de Vehiculos Motocicleta")
                    for vehiculo in lista_moto:
                        print(vehiculo[1])
                          
                          
        except FileNotFoundError:
            print(f"No es posible leer el archivo {self.archivo}.{self.formato} porque no existe un archivo con este nombre")


        except Exception as e:
            print("Error: ", e)

class AutoCarga(Automovil):
    
    archivo = "autoscarga" 
    formato = "csv"
    
    def __init__(self, marca:str, modelo:str, num_ruedas:int, velocidad:int, cilindrada:int, peso_carga:int) -> None:
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga
        
    def __str__(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.num_ruedas} ruedas, {self.velocidad} km/h, {self.cilindrada} cc, Carga: {self.peso_carga}"      
    
    
#Contenido Parte 3 de la Prueba de consolidación     
    @classmethod
    def guardar_datos_csv(self, autocarga_o_lista):
        """ Guarda los datos de una instancia de vehículo o de una lista/tupla de instancias de clase en un archivo csv.
            Si el archivo no existe, lo crea; si ya existe, añade los datos al archivo sin sobreescribirlo.
            Se guarda cada instancia con su nombre de la clase y un diccionario con sus atributos.

        
        Args:
        vehiculo_o_lista : Este atributo puede ser una única instancia de clase o una lista o tupla de instancias.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "a", newline= "\n", encoding= "utf-8") as nuevo_archivo:
                writer = csv.writer(nuevo_archivo)
                
                
                
                if isinstance (autocarga_o_lista, list) or isinstance(autocarga_o_lista, tuple):
                    for autocarga in autocarga_o_lista:
                        fila = [(autocarga.__class__, autocarga.__dict__)]
                        writer.writerow(fila)
                else:
                    autocarga = autocarga_o_lista
                    fila = [(autocarga.__class__, autocarga.__dict__)]         
                    writer.writerow(fila)
                    
                    
        except FileNotFoundError:
            print(f"No es posible crear o guardar contenido en el archivo {self.archivo}.{self.formato} ya que no se encuentra la ruta o directorio {ruta} que lo contiene.")
    
        except Exception as e:
            print("Error: ", e)
            
    
    @classmethod
    def leer_datos_csv(self):
        """Lee el archivo existente que almacena la información para la clase AutoCarga. La información contenida se clasificará según la clase a la que pertenece cada instancia y se imprimira en terminal.
           Dada su clasificación, se excluira la impresión directa sobre la propia clase para cada instancia.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "r") as nuevo_archivo:
                reader = csv.reader(nuevo_archivo)
                
            
                lista_auto = []
                lista_autoparticular = []
                lista_autocarga = []    
                lista_bici = []
                lista_moto = []
                
                    
                for fila in reader:
                    fila = str(fila)
                    if "Automovil" in fila:
                        fila = fila.rstrip(')"]')
                        lista_auto.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoParticular" in fila:
                        fila = fila.rstrip(')"]')
                        lista_autoparticular.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoCarga" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_autocarga.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Bicicleta" in (fila):
                        fila = fila.rstrip(')"]')
                        lista_bici.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Motocicleta" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_moto.append(list(fila.split(",", maxsplit = 1)))
                        
                                     
                    else: 
                        print("No se encuentra el tipo de vehiculo")
               
               #Se imprimen las listas si existen. Se excluye su clase en la impresión.
                if lista_auto:
                    print("\nLista de Vehiculos Automovil")
                    for vehiculo in lista_auto:
                        print(vehiculo [1])
                        
                if lista_autoparticular:
                    print("\nLista de Vehiculos Particular")
                    for vehiculo in lista_autoparticular:
                        print(vehiculo[1])
                          
                if lista_autocarga:
                    print("\nLista de Vehiculos Carga")
                    for vehiculo in lista_autocarga:
                        print(vehiculo[1])
                        
                if lista_bici:
                    print("\nLista de Vehiculos Bicicleta")
                    for vehiculo in lista_bici:
                        print(vehiculo[1])
                          
                if lista_autoparticular:
                    print("\nLista de Vehiculos Motocicleta")
                    for vehiculo in lista_moto:
                        print(vehiculo[1])
                          
                          
        except FileNotFoundError:
            print(f"No es posible leer el archivo {self.archivo}.{self.formato} porque no existe un archivo con este nombre")


        except Exception as e:
            print("Error: ", e)            
                
class Bicicleta(Vehiculo):
    
    archivo = "bicicletas" 
    formato = "csv"
    
    def __init__(self, marca:str, modelo:str, num_ruedas:int, tipo = ("Urbana o Carrera")) -> None:
        super().__init__(marca, modelo, num_ruedas)
        
        tipos_permitidos = ["Urbana", "Carrera"]
        if tipo not in tipos_permitidos:
            raise Exception ("El tipo de Bicicleta es invalido. Ingresa una ocpión valida\n Urbana o Carrera")#Hay que modificar esto, hacerlo mas especifico
        
        self.tipo = tipo
    
    def __str__(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.num_ruedas} ruedas, Tipo: {self.tipo}" 


#Contenido Parte 3 de la Prueba de consolidación             
    @classmethod
    def guardar_datos_csv(self, bicicleta_o_lista):
        """ Guarda los datos de una instancia de vehículo o de una lista/tupla de instancias de clase en un archivo csv.
            Si el archivo no existe, lo crea; si ya existe, añade los datos al archivo sin sobreescribirlo.
            Se guarda cada instancia con su nombre de la clase y un diccionario con sus atributos.

        
        Args:
        vehiculo_o_lista : Este atributo puede ser una única instancia de clase o una lista o tupla de instancias.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "a", newline= "\n", encoding= "utf-8") as nuevo_archivo:
                writer = csv.writer(nuevo_archivo)
                
                
                
                if isinstance (bicicleta_o_lista, list) or isinstance(bicicleta_o_lista, tuple):
                    for bicicleta in bicicleta_o_lista:
                        fila = [(bicicleta.__class__, bicicleta.__dict__)]
                        writer.writerow(fila)
                else:
                    bicicleta = bicicleta_o_lista
                    fila = [(bicicleta.__class__, bicicleta.__dict__)]         
                    writer.writerow(fila)
                    
                    
        except FileNotFoundError:
            print(f"No es posible crear o guardar contenido en el archivo {self.archivo}.{self.formato} ya que no se encuentra la ruta o directorio {ruta} que lo contiene.")
   
        except Exception as e:
            print("Error: ", e)
     
    
    @classmethod
    def leer_datos_csv(self):
        """Lee el archivo existente que almacena la información para la clase Bicicleta. La información contenida se clasificará según la clase a la que pertenece cada instancia y se imprimira en terminal.
           Dada su clasificación, se excluira la impresión directa sobre la propia clase para cada instancia.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "r") as nuevo_archivo:
                reader = csv.reader(nuevo_archivo)
                
            
                lista_auto = []
                lista_autoparticular = []
                lista_autocarga = []    
                lista_bici = []
                lista_moto = []
                
                    
                for fila in reader:
                    fila = str(fila)
                    if "Automovil" in fila:
                        fila = fila.rstrip(')"]')
                        lista_auto.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoParticular" in fila:
                        fila = fila.rstrip(')"]')
                        lista_autoparticular.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoCarga" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_autocarga.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Bicicleta" in (fila):
                        fila = fila.rstrip(')"]')
                        lista_bici.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Motocicleta" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_moto.append(list(fila.split(",", maxsplit = 1)))
                        
                                     
                    else: 
                        print("No se encuentra el tipo de vehiculo")
               
               #Se imprimen las listas si existen. Se excluye su clase en la impresión.
                if lista_auto:
                    print("\nLista de Vehiculos Automovil")
                    for vehiculo in lista_auto:
                        print(vehiculo [1])
                        
                if lista_autoparticular:
                    print("\nLista de Vehiculos Particular")
                    for vehiculo in lista_autoparticular:
                        print(vehiculo[1])
                          
                if lista_autocarga:
                    print("\nLista de Vehiculos Carga")
                    for vehiculo in lista_autocarga:
                        print(vehiculo[1])
                        
                if lista_bici:
                    print("\nLista de Vehiculos Bicicleta")
                    for vehiculo in lista_bici:
                        print(vehiculo[1])
                          
                if lista_autoparticular:
                    print("\nLista de Vehiculos Motocicleta")
                    for vehiculo in lista_moto:
                        print(vehiculo[1])
                          
                          
        except FileNotFoundError:
            print(f"No es posible leer el archivo {self.archivo}.{self.formato} porque no existe un archivo con este nombre")

        except Exception as e:
            print("Error: ", e)        
            
class Motocicleta(Bicicleta):
    
    archivo = "motocicletas" 
    formato = "csv"
    
    def __init__(self, marca:str, modelo:str, num_ruedas:int, tipo= "Urbana o Carrera", num_radios = "21 radios", cuadro = ("Doble cuna, Multitubolar o Doble viga"), motor =("2T o 4T")) -> None:
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.num_radios = num_radios
        
        cuadros_permitidos = ["Doble cuna", "Multitubolar","DobleViga"]
        if cuadro not in cuadros_permitidos:
            raise Exception ("El tipo de cuadro es invalido. Ingresa una ocpión valida\n Doble cuna, Multitubolar o Doble viga")
        
        self.cuadro = cuadro
        
        motores_permitidos = ["2T", "4T"]                     
        if motor not in motores_permitidos:
            raise Exception ("El tipo de motor es invalido. Ingresa una ocpión valida\n 2T o 4T")
        
        self.motor = motor    
     
    def __str__(self) -> str:
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.num_ruedas} ruedas, Tipo: {self.tipo}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.num_radios}"


#Contenido Parte 3 de la Prueba de consolidación 
    @classmethod
    def guardar_datos_csv(self, motocicleta_o_lista):
        """ Guarda los datos de una instancia de vehículo o de una lista/tupla de instancias de clase en un archivo csv.
            Si el archivo no existe, lo crea; si ya existe, añade los datos al archivo sin sobreescribirlo.
            Se guarda cada instancia con su nombre de la clase y un diccionario con sus atributos.

        
        Args:
        vehiculo_o_lista : Este atributo puede ser una única instancia de clase o una lista o tupla de instancias.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "a", newline= "\n", encoding= "utf-8") as nuevo_archivo:
                writer = csv.writer(nuevo_archivo)
                
                
                
                if isinstance (motocicleta_o_lista, list) or isinstance(motocicleta_o_lista, tuple):
                    for motocicleta in motocicleta_o_lista:
                        fila = [(motocicleta.__class__, motocicleta.__dict__)]
                        writer.writerow(fila)
                else:
                    motocicleta = motocicleta_o_lista
                    fila = [(motocicleta.__class__, motocicleta.__dict__)]         
                    writer.writerow(fila)
                    
                    
        except FileNotFoundError:
            print(f"No es posible crear o guardar contenido en el archivo {self.archivo}.{self.formato} ya que no se encuentra la ruta o directorio {ruta} que lo contiene.")
            
        except Exception as e:
            print("Error: ", e)
 
    @classmethod
    def leer_datos_csv(self):
        """Lee el archivo existente que almacena la información para la clase Motocicleta. La información contenida se clasificará según la clase a la que pertenece cada instancia y se imprimira en terminal.
           Dada su clasificación, se excluira la impresión directa sobre la propia clase para cada instancia.
        """
  
        try:
            ruta = "./archivos/"
            nom_archivo = f"{self.archivo}.{self.formato}"
            path = ruta + nom_archivo
            
            with open(path, "r") as nuevo_archivo:
                reader = csv.reader(nuevo_archivo)
                
            
                lista_auto = []
                lista_autoparticular = []
                lista_autocarga = []    
                lista_bici = []
                lista_moto = []
                
                    
                for fila in reader:
                    fila = str(fila)
                    if "Automovil" in fila:
                        fila = fila.rstrip(')"]')
                        lista_auto.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoParticular" in fila:
                        fila = fila.rstrip(')"]')
                        lista_autoparticular.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "AutoCarga" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_autocarga.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Bicicleta" in (fila):
                        fila = fila.rstrip(')"]')
                        lista_bici.append(list(fila.split(",", maxsplit = 1)))
                        
                        
                    elif "Motocicleta" in(fila):
                        fila = fila.rstrip(')"]')
                        lista_moto.append(list(fila.split(",", maxsplit = 1)))
                        
                                     
                    else: 
                        print("No se encuentra el tipo de vehiculo")
               
               #Se imprimen las listas si existen. Se excluye su clase en la impresión.
                if lista_auto:
                    print("\nLista de Vehiculos Automovil")
                    for vehiculo in lista_auto:
                        print(vehiculo [1])
                        
                if lista_autoparticular:
                    print("\nLista de Vehiculos Particular")
                    for vehiculo in lista_autoparticular:
                        print(vehiculo[1])
                          
                if lista_autocarga:
                    print("\nLista de Vehiculos Carga")
                    for vehiculo in lista_autocarga:
                        print(vehiculo[1])
                        
                if lista_bici:
                    print("\nLista de Vehiculos Bicicleta")
                    for vehiculo in lista_bici:
                        print(vehiculo[1])
                          
                if lista_autoparticular:
                    print("\nLista de Vehiculos Motocicleta")
                    for vehiculo in lista_moto:
                        print(vehiculo[1])
                          
                          
        except FileNotFoundError:
            print(f"No es posible leer el archivo {self.archivo}.{self.formato} porque no existe un archivo con este nombre")

        except Exception as e:
            print("Error: ", e)
 
 
