
from Inicio import proveedor1
class Archivo():
    def __init__(self, nombre, datos,separador="|"):
        self.nombre=nombre
        self.separador=separador
        self.datos=datos
    def escribir(self):
        with open(self.nombre,'a') as w:
            lista=[self.datos]
            for dat in lista:
                w.write(dat+"\n")

arch=Archivo("txt/luis.txt",proveedor1.GetdatosString())
arch.escribir()




    
    
        