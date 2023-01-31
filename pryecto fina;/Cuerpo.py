from abc import ABC,abstractmethod
from datetime import datetime, time, date
import time


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

class Provedor(Persona):
    def __init__(self,nom,estado, direcion, phone, credit):
        super().__init__(nom, estado)
        self.direcion=direcion
        self.telefono=phone
        self.credito=credit
        
    def GetdatosString(self):
        return f'{str(self.nombre)}|{ str(self.direcion)}|{str(self.credito)}|{str(self.estado)}|{ str(self.telefono)}'
    def mostrarDatos(self):
        pass

    @staticmethod
    def getCredito():
        return "Credito aprobado"

class Compra:
    _id = 0

    def __init__(self, fecha, estado, vt, proveedor):
        Compra._id += 1
        self.__idCompra = Compra._id
        self.fecha_compra=fecha
        self.valorTotal=vt
        self.estado=estado
        self.proveedor=proveedor

    @property
    def id(self):
        return self.__idCompra


    def mostrarDatos(self):
        print(self.valorTotal,self.estado,self.proveedor.id,self.proveedor.nombre)
        dat=input("")

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
        pass

    def Intereses(self,interez):
        pass

    def mostrarDatos(self):
        print(self.cuota,self.estado, self.fecha)


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


    def aggDeuda(self,aamm,valor,est=True):
        detalle=DetalleDeuda(aamm,valor,est)
        #self.detalleDeuda=detalle
        #procesos
        #calculos 
        self.detalleDeuda.append(detalle)

    def mostrarDatos(self):
        print(self.valorCredito,self.NoCuota, self.valorCuota, self.compra.fecha_compra,self.compra.proveedor.nombre)
        for det in self.detalleDeuda:
           print(det.id,det.fecha,det.cuota)
        





#C1=Compra("01-02-2022",True, 23,proveedor1)
#C1.mostrarDatos()
#proveedor1.mostrarDatos()
#print(Proveedor.getCredito())
#ded= Deuda(True,C1,"01-01-2022",200,10,20 )
#ded.aggDeuda("202301",100)
#ded.aggDeuda("202302",100)
#ded.mostrarDatos()
#print(proveedor1.GetdatosString())
