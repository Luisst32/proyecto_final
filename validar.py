import time
from helper import coord
from helper import *
class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            coord(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                coord(col,fil);print(mensajeError)
               
                
                time.sleep(2)
                coord(col,fil);print(" "*20)
        return valor

    def solo_letras(self,mensajeError,col,fil): 
        while True:
            coord(col,fil)  
            valor = str(input())
            if valor.isalpha():
                break
            else:
                coord(col,fil);print(mensajeError)
                time.sleep(2)
                coord(col,fil);print(" "*20)
                
        return valor

    def solo_decimales(self,mensajeError,col, fil):
        while True:
            coord(col,fil)  
            valor = str(input())
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                coord(col,fil);print(mensajeError)
               
                
                time.sleep(2)
                coord(col,fil);print(" "*20)
        return valor
    def solo_boleanos(self,mensajeError,col,fil):
        while True:
            coord(col,fil)  
            valor =input()
            try:
                if valor.lower()=="true" or valor.lower()=="false":
                    break
                else:
                    raise ValueError(mensajeError)
            except ValueError as error:
                coord(col,fil);print(error)
                time.sleep(2)
                coord(col,fil);print(" "*20)

        return valor
    


    def cedula():
        pass
    
class otra:
    pass    
