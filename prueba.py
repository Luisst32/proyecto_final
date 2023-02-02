
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



   
              