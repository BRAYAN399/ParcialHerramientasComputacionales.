codigo= input("codigo del producto: ")
cant=int(input("cantidad de unidades: "))
precio=int(input("ingresa el precio del producto: "))
inf_cliente=int(input("si es profesor digite [1],    si es estudiante digite [2]: "))
cedula=int(input("numero de cedula: "))


if inf_cliente==1:
    valor=precio*0.8*cant
    print (" el profesor con cedula ",cedula," debe pagar", valor," por el",codigo,)
elif inf_cliente==2:
    valor=precio*0.6*cant
    print(" el profesor con cedula ",cedula," debe pagar", valor," por el producto",codigo,)
else:
    print ("no se ha especificado si es estudiante o profesor, por favor, intente de nuevo")
    
    
        
