import os
import time


def borrarPantalla():
 os.system("cls")

def coord(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

def salir():
    borrarPantalla()
    coord(27,2);print("Que tenga buen Dia.")

    time.sleep(4)
    exit()


