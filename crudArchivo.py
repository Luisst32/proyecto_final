
from helper import *
class Archivo():
    def __init__(self, nombre, separador="|",pro=""):
        self.__nombre=nombre
        self.__separador=separador
        self.pro=pro
    def leer(self):
        try:
         with open(self.__nombre, 'r', encoding="UTF-8") as file:
            lista=[]
            for linea in file:
                line = linea[:-1].split(self.__separador)
                lista.append(line)
        except IOError:
         lista=[] 
        return lista  

    def escribir(self,datos,modo):
        with open(self.__nombre, modo, encoding="UTF-8") as file:
            for dato in datos:
                file.write(dato+'\n')
    def proArch(self):
        with open(self.__nombre, "r") as file:  
            for line in file:
               values = line.strip().split("|")
               coord(33,1);print("Proveedor")
               coord(27,2);print("Fila:", values[0])
               coord(27,3);print("Nombre:", values[1])
               coord(27,4);print("Direccion:", values[2])
               coord(27,5);print ("Credito:",values[3])
               coord(27,6);print ("Estado:",values[4])
               coord(27,7);print ("Telefono:",values[5])
               
         
               break
        s_n2=input("continuar s/n ")
        if s_n2.upper()=="S":
            return
        if s_n2.upper()=="N":
            salir()

    def compArch(self):
        with open("txt/dat_proveedores.txt", "r") as file: 
            for line in file:
                values = line.strip().split("|")
                coord(27,3);print("Proverdor:", values[1])
                break

        with open(self.__nombre, "r") as file:
           for line in file:
              values = line.strip().split("|")
              coord(33,1);print("Compra")
              coord(27,4);print("Fecha:", values[0])
              coord(27,5);print("Estado:", values[1])
              coord(27,6);print ("Valor Total: ",values[2])
              
              break
        s_n2=input("continuar s/n ")
        if s_n2.upper()=="S":
            return
        if s_n2.upper()=="N":
            salir()


















   # def mostrar_datos(self, num_fila,fila="",nombre="",direccion="",credito="",estado="",telefono=""):
    #    with open(self.__nombre, "r") as archivo:
     #       lineas = archivo.readlines()
      #      datos = lineas[num_fila - 1].strip().split("|")
       #     fila = datos[0]
        #    nombre = datos[1]
         #   direccion = datos[2]
        #   credito= datos[3]
         #   estado= datos[4]
          #  telefono= datos[5]
        #print("Fila:", fila)
        #print("Nombre:", nombre)
        #print("Direccion:", direccion)
        #print("Credito:", credito)
        #print("Estado:", estado)
        #print("Telefomo:", telefono)
        ##s_n=input("continuar s/n ")
        #if s_n=="s":
        #    return
        #if s_n=="n":
        #    exit()
   







    
    
        