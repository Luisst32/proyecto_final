from helper import *
from crudArchivo import Archivo
from Cuerpo import Proveedor,Compra,Deuda,DetalleDeuda
import time
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
        inp=input("|  Ingrese una opcion|1..5| ->")
        return inp
    def Provedor(self):
        borrarPantalla()
        coord(33,1);print("Provedor ")
        coord(27,2);print("1-Mostrar Datos ")
        #coord(27,3);print("2-Agregar Proveedor ")
        coord(27,3);print("2-Obtener Credito ")
        coord(22,5);dat=input("Ingrese una opcion:")
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
        coord(27,3);opc=input("Ingrese una opcion: ")
        if opc=="1":
            borrarPantalla()
            com=Compra("","","","")
            com.mostrarDatos()

        
        
    def Deuda(self):
        borrarPantalla()
        coord(33,1);print("Deuda ")
        coord(27,2);print("1-Mostrar Deuda ")
        coord(27,3);print("2-Agregar Deuda ")
        dat3=input("Ingrese una opcion:")
        if dat3=="1":
            borrarPantalla()
            coord(27,2);print("1-Mostrar todas las deudas")
            coord(27,3);print("2-Mostrar por filas")
            dat4=input("Ingrese una opcion: ")
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
            coord(33,1);print("Agregar Datos ")
            coord(27,2);fechacred=input("Ingrese la fecha del credito: ")
            coord(27,3);valorcred=input("Ingrese el valor del credito: ")
            coord(27,4);nocuotas=input("Numero de cuotas: ")
            coord(27,5);valorcuotas=input("Valor de las cuotas: ")
            coord(27,7);estado=input("Estado: ")
            coord(27,8);compra=input("Compra: ")
            arprov=Archivo("txt/dat_deuda.txt","|")
            proveedores=arprov.leer()
            pro = Deuda(estado,compra, fechacred, valorcred, nocuotas,valorcuotas)
            datos = [pro.aggDeuda()]
            arprov = Archivo("txt/dat_deuda.txt","|")
            arprov.escribir(datos,"a")
            coord(27,8);print("Guardado exitosamente.")
            time.sleep(2)







    def Conusulta_Generales(self):
        borrarPantalla()
        print("Consulta Generales")
        print("1-Mostrar detalles de la deuda")
        dat5=input("Ingrese una opcion: ")
        if dat5=="1":
            borrarPantalla()
            try:
                with open("txt/dat_deuda.txt", "r") as file:
                    con=0
                    for line in file:
                        con+=1
                    coord(33,1);print("Agregar por filas ","[",con,"]Filas actualmente",)
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
            capital=float(nocuotas)*float(valorcuotas)
            an=float(nocuotas)/12
            tasaintere=0.12
            intere=capital*tasaintere*an
            pagototal=intere+float(valorcuotas)
            det=DetalleDeuda(fecha,nocuotas,estado)
            det.Intereses(intere)
            det.Pago(pagototal)
            det.mostrarDatos()




            


            with open("txt/dat_deuda.txt", "r") as file:
             for line in file:
                 values = line.strip().split("|")
                 cuotas=values[5]
                 break
            print(int(cuotas))
            a=input("")





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
    #aqui pon los otros menus de las opciones, le puse salir porque ya no hace nada despues de eso
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


    