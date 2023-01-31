from helper import *
from Cuerpo import Provedor



class Menu:
    def __init__(self, titulo="",opciones=[],col=33,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
    def menu(self):
        #esto es para poder ubicar el texto en cualquier lugar de la consla: col-fil
        coord(self.col,self.fil);print(self.titulo)
        #---------------------------------------------------------------------------
        print("                          |\n                          |\n                          |\n                          |\n                          |")
        for opci in self.opciones:
            self.fil+=1
            coord(self.col,self.fil),print(opci)
        coord(self.col-6,self.fil+2)
        inp=input("|  Ingrese una opcion|1..5| ->")
        return inp




inp=''

while inp !='5':
    borrarPantalla()
    menu=Menu("   Menu",["1-Proveedor","2-Compra","3-Deuda cuotas","4-Cunsulta Genereles","5-Salir"])
    inp=menu.menu()
    #aqui pon los otros menus de las opciones, le puse salir porque ya no hace nada despues de eso
    if inp=="1":
        
        
        borrarPantalla()
        coord(33,1);print("Provedor ")
        coord(27,2);print("1-Mostrar Datos ")
        coord(27,3);print("2-Agregar Proveedor ")
        dat=input("Ingrese una opcion:")
        if dat=="1":
            
            
            dat2=input("Regresar[Y|N]:")
            if dat2.lower=="y":
                inp.menu()
            if dat2=="n":
                salir()
        if dat=="2":
            borrarPantalla()
            


            coord(33,1);print("Agregar Provedor")
            
            
            nomb=input("Nombre: ")
            est=input("Estado: ")
            fech=input("Fecha: ")
            nume=input("Numero: ")
            cred=input("Credito: ")
            proveedor1=Provedor("luis","sds", "ds", "ds", "Dsd")
           
           
            


            


        
    if inp=="2":
        borrarPantalla()
        print("Compra")
        salir()
    if inp=="3":
        borrarPantalla()
        coord(33,1);print("Deuda ")
        coord(27,2);print("1-Mostrar Datos ")
        coord(27,2);print("2-Agregar Deuda ")
        dat3=input("Ingrese una opcion:")

    if inp=="4":
        borrarPantalla()
        print("Consulra Generales")
        salir()
    if inp=="5":
        borrarPantalla()
        coord(35,2);print("Gracias por su visita.")
        coord(33,3);print("❀-----------------------❀")
        salir()

        

    





    


