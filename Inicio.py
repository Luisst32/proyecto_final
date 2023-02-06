from helper import *
from crudArchivo import Archivo
from Cuerpo import Proveedor,Compra,Deuda,DetalleDeuda
import time
from validar import Valida
class Menu:
    def __init__(self, titulo="",opciones=[],col=33,fil=2):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
    def menu(self):
        #esto es para poder ubicar el texto en cualquier lugar de la consla: col-fil
        coord(self.col,self.fil);print(self.titulo)

        for opci in self.opciones:
            self.fil+=1
            coord(self.col,self.fil),print(opci)
        coord(self.col-6,self.fil+2)
        v=Valida()
        print("|  Ingrese una opcion|1..5| ->")
        validar=v.solo_numeros("Solo se permiten numeros",58,6)
        return validar
    def Provedor(self):
        borrarPantalla()
        coord(33,1);print("Provedor ")
        coord(27,2);print("1-Mostrar Datos ")
      
        coord(27,3);print("2-Obtener Credito ")
        coord(22,5);print("Ingrese una opcion: ")
        v=Valida()
        dat=v.solo_numeros("Solo se permiten numeros",42,5)
        if dat=="1":
            borrarPantalla()
            prov=Proveedor("","","","","","")
            prov.mostrarDatos()
    
        if dat=="2":
            borrarPantalla()
            pro=Proveedor("","","","","","")
            pro.getCredito()











    def Compra(self):
        borrarPantalla()
        coord(33,1);print("Compra ")
        coord(27,2);print("1-Mostrar Datos ")
        
        v=Valida()
        coord(27,3);print("Ingrese una opcion: ")
        opc=v.solo_numeros("Solo se permiten numeros",47,3)
        if opc=="1":
            borrarPantalla()
            com=Compra("","","","")
            com.mostrarDatos()

        
        
    def Deuda(self):
        borrarPantalla()
        coord(33,1);print("Deuda ")
        coord(27,2);print("1-Mostrar Deuda ")
        coord(27,3);print("2-Agregar Deuda ")
        
        v=Valida()
        coord(27,5);print("Ingrese una opcion:")
        dat3=v.solo_numeros("Solo se permiten numeros",47,5)
        if dat3=="1":
            borrarPantalla()
            coord(27,2);print("1-Mostrar todas las deudas")
            coord(27,3);print("2-Mostrar por filas")
            coord(27,5);print("Ingrese una opcion: ")
            v=Valida()
          
            dat4=v.solo_numeros("Solo se permiten numeros",48,5)

            
            if dat4=="1":
                borrarPantalla()
                deu=Deuda("","","","","","")
                deu.mostrarDatos("1")
            if dat4=="2":
                borrarPantalla()
                deu=Deuda("","","","","","")
                deu.mostrarDatos("2")


        if dat3=="2":
            borrarPantalla()
            v=Valida()
            coord(33,1);print("Agregar Datos ")
            coord(27,2);fechacred=input("Ingrese la fecha del credito:")
         

            coord(27,3);print("Ingrese el valor del credito: ")
            valorcred=v.solo_decimales("Solo numeros/decimales",57,3)

            coord(27,4);print("Numero de cuotas: ")
            nocuotas=v.solo_numeros("Solo numeros",57,4)
  
            coord(27,5);print("Valor de las cuotas: ")
            valorcuotas=v.solo_decimales("Solo numeros/decimales",57,5)

            coord(27,6);print("Estado: ")
            estado=v.solo_boleanos("Solo boleanos",57,6)

            coord(27,8);print("Compra: ")
            compra=v.solo_letras("Solo letras",57,7)

            pro = Deuda(estado,compra, fechacred, valorcred, nocuotas,valorcuotas)
            pro.GetdatosString()
            datos = [pro.GetdatosString()]
            pro.aggdeuda(fechacred,valorcred,estado,datos)

            #arprov = Archivo("txt/dat_deuda.txt","|")
            #arprov.escribir(datos,"a")
            #coord(27,8);print("Guardado exitosamente.")
            #time.sleep(2)







    def Conusulta_Generales(self):
        borrarPantalla()
        coord(33,1);print("Consulta Generales")
        coord(27,2);print("1-Mostrar detalles de la deuda")
    
        v=Valida()
        coord(27,5);print("Ingrese una opcion: ")
        dat5=v.solo_numeros("Solo  numeros",48,5)
        
        if dat5=="1":
            borrarPantalla()
            try:
                with open("txt/dat_deuda.txt", "r") as file:
                    con=0
                    for line in file:
                        con+=1
                    coord(33,1);print("Mostrar por filas ","[",con,"]Filas actualmente",)
                    coord(27,2);num_fila = int(input("Ingrese numero de fila que desee saber sus detalles: "))
                    with open("txt/dat_deuda.txt", "r") as archivo:
                        lineas = archivo.readlines()
                        datos = lineas[num_fila - 1].strip().split("|")
                        estado=datos[1]
                        fecha=datos[3]
                        nocuotas= datos[5]
                        valorcuotas=datos[6]

            except:
                print("!! Fuera de rango o caracter no valido !!")
                time.sleep(4)
                return
            borrarPantalla()
            tasa_interes=0.50
            valort=float(valorcuotas)*float(nocuotas)
            x=DetalleDeuda(fecha,estado,float(nocuotas))
            x.Intereses(tasa_interes,float(valorcuotas))
            x.Pago(valort)
            x.mostrarDatos()

            
        


            





    def Salir(self):
        borrarPantalla()
        coord(35,2);print("Gracias por su visita.")
        coord(33,3);print("❀-----------------------❀")
        salir()
inp=''
while inp !='5':
    borrarPantalla()
    menu=Menu("   Menu",["1-Proveedor","2-Compra","3-Deuda cuotas","4-Cunsulta Genereles","5-Salir"])
    inp=menu.menu()

    if inp=="1":
        menu.Provedor()    
    if inp=="2":
        menu.Compra()
    if inp=="3":
        menu.Deuda()
    if inp=="4":
        menu.Conusulta_Generales()
    if inp=="5":
        menu.Salir()


    