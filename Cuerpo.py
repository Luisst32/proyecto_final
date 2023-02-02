from abc import ABC,abstractmethod
from datetime import datetime, time, date
import time
from crudArchivo import Archivo
from helper import *




class Persona(ABC):
    _secuencia=0
    def __init__(self,nom,estado):
        Persona._secuencia=Persona._secuencia+1
        self.__id=Persona._secuencia
        self.nombre = nom
        self.estado= estado
    

    @property
    def id(self):
        return self.__id
    @abstractmethod 
    def mostrarDatos(self):
        pass

class Proveedor(Persona):
    def __init__(self,ids,nom,estado, direcion, phone, credit):
        super().__init__(nom, estado)
        self.ids=ids
        self.direcion=direcion
        self.telefono=phone
        self.credito=credit
        
    def GetdatosString(self):
        return f'{str(self.ids)}|{str(self.nombre)}|{ str(self.direcion)}|{str(self.credito)}|{str(self.estado)}|{ str(self.telefono)}'
    def mostrarDatos(self):
        borrarPantalla()
        prov=Archivo("txt/dat_proveedores.txt","|")
        prov.proArch()
        


        
    @staticmethod
    def getCredito():
        credi=""
        with open("txt/dat_proveedores", "r") as file:
            con=0
            for line in file:
                con+=1
                values = line.strip().split("|")
                print("----------",con,"--------------")
                print("Nombre:", values[1])
                if float(values[3])>=1000:
                    credito="Aprobado"
                if float(values[3])<1000:
                    credito="No aprobado"
                print("Credito:", credito)
                break
        s_n2=input("continuar s/n ")
        if s_n2.upper()=="S":
            return
        if s_n2.upper()=="N":
            salir()

        
   

class Compra:
    _id = 0

    def __init__(self, fecha, estado, vt, proveedor):
        Compra._id += 1
        self.__idCompra = Compra._id
        self.fecha_compra=fecha
        self.valorTotal=vt
        self.estado=estado
        self.proveedor=proveedor

    def GetdatosString(self):
        return f'{str(self.fecha_compra)}|{str(self.estado)}|{ str(self.valorTotal)}|{str(self.proveedor)}'

    @property
    def id(self):
        return self.__idCompra


    def mostrarDatos(self):
        borrarPantalla()
        coord(27,2);print("id: ",self.__idCompra)
        
        com=Archivo("txt/dat_compra.txt","|")
        com.compArch()
        
        

       




class Calculo(ABC): #interface
    
    @abstractmethod
    def mostrarDatos():
        pass
   


class DetalleDeuda(Calculo):
    _id = 0

    def __init__(self, fecha, cuota, estado):
        DetalleDeuda._id += 1
        self.__idDetalleDeuda = DetalleDeuda._id
        self.fecha=fecha
        self.cuota=cuota
        self.estado=estado

    @property
    def id(self):
        return self.__idDetalleDeuda

    def Pago(self, valor):
        return print("El valor total es: ", valor)

    def Intereses(self,intere):
        return print("El interes es: ", intere)

    def mostrarDatos(self):
        return print("cuota: ",self.cuota,"Estado: ",self.estado,"Fecha: " ,self.fecha)


class Deuda:
    _idDeuda = 0
    
    def __init__(self,  estado, compra, fecha, vCred, Ncuotas,vCuot ):
        Deuda._idDeuda = Deuda._idDeuda + 1
        self.__idDeuda = str(Deuda._idDeuda)
        
        self.fecha_credito = fecha
        self.compra=compra
        self.valorCredito = vCred
        self.NoCuota=Ncuotas
        self.valorCuota=vCuot
        self.detalleDeuda = []
       
        
        self.estado=estado

    @property
    def id(self):
        return self.__idDeuda


    def aggDeuda(self):
        return f'{str(self.__idDeuda)}|{str(self.estado)}|{ str(self.compra)}|{str(self.fecha_credito)}|{str(self.valorCredito)}|{str(self.NoCuota)}|{str(self.valorCuota)}'



    def calculo(self):
        with open("txt/dat_deuda.txt", "r") as file:
            for line in file:
                values = line.strip().split("|")
                cuotas=values[5]
                break
            print(int(cuotas))
            






        #detalle=DetalleDeuda(aamm,valor,est)
        #self.detalleDeuda=detalle
        #procesos
        #calculos 
        #self.detalleDeuda.append(detalle)

    def mostrarDatos(self,op):
        if op=="1":
            with open("txt/dat_deuda.txt", "r") as file:
              con=0
              for line in file:
                  con+=1
                  values = line.strip().split("|")
                  print("------------",con,"---------------")
                  print("id :", values[0])
                  print("Estado :", values[1])
                  print("Compra :", values[2])
                  print("Fecha del credito :", values[3])
                  print("Valor del credito :", values[4])
                  print("Numero cuotas :", values[5])
                  print("Valor cuotas :", values[6])
            s_n=input("Continuar s/n ")
            if s_n.upper()=="S":
               return
            if s_n.upper()=="N":
               salir()  
        if op=="2":
            try:
                with open("txt/dat_deuda.txt", "r") as file:
                    con=0
                    for line in file:
                        con+=1
                coord(33,1);print("Agregar por filas ","[",con,"]Filas actualmente",)
                coord(27,2);num_fila = int(input("Ingrese numero de fila: "))
                with open("txt/dat_deuda.txt", "r") as archivo:
                    lineas = archivo.readlines()
                    datos = lineas[num_fila - 1].strip().split("|")
                    idSig = datos[0]
                    estado = datos[1]
                    compra = datos[2]
                    fechacred= datos[3]
                    valorcred= datos[4]
                    nocuotas= datos[5]
                    valorcuotas=datos[6]

                borrarPantalla()
                coord(27,2);print("Fila :", idSig)
                coord(27,3);print("Estado :", estado)
                coord(27,4);print("Compra :", compra)
                coord(27,5);print("Fecha del credito :", fechacred)
                coord(27,6);print("Valor del credito :", valorcred)
                coord(27,7);print("Numero de cuotas :", nocuotas)
                coord(27,8);print("Valor de las cuotas :", valorcuotas)
                s_n=input("Continuar s/n ")
                if s_n.upper()=="S":
                    return
                if s_n.upper()=="N":
                    salir()   

            except:
                print("!! Fuera de rango o caracter no valido !!")
                time.sleep(4)
                return

        
        #for det in self.detalleDeuda:
        #   print(det.id,det.fecha,det.cuota)
        





#C1=Compra("01-02-2022",True, 23,proveedor1)
#C1.mostrarDatos()
#proveedor1.mostrarDatos()
#print(Proveedor.getCredito())
#ded= Deuda(True,C1,"01-01-2022",200,10,20 )
#ded.aggDeuda("202301",100)
#ded.aggDeuda("202302",100)
#ded.mostrarDatos()
#print(proveedor1.GetdatosString())
