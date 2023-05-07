from ClaseViajeroFrecuente import ViajeroFrecuente
import csv

    
if __name__=="__main__":
    listaViajero=[]
    archivo=open("Viajeros.csv")
    reader= csv.reader(archivo,delimiter=",")
    bandera=True
    for fila in reader:
        if bandera:
            bandera=not bandera
    
        else:
            numero =fila[0]
            dni =fila[1]
            nom =fila[2]
            ape =fila[3]
            millas =int(fila[4])
            unViajero=ViajeroFrecuente(numero,dni,nom,ape,millas)
            listaViajero.append(unViajero)
    archivo.close()
    for i in range(len(listaViajero)):
               print(listaViajero[i])

    num=int(input("ingrese el numero de viajero >> "))
    i=0
    viajeroNuevo=listaViajero[0]
    numero=int(viajeroNuevo.getNumero())
    print(numero)
    #print(type(numero))
    #print(type(num))
    while ((i<(len(listaViajero)-1))and(num!=numero)):
        i+=1
        viajeroNuevo=listaViajero[i]
        numero=int(viajeroNuevo.getNumero())
        print(numero)
    
        
    print("mostrar cantidad de millas {}:".format(viajeroNuevo.cantidadYotaldeMillas()))

    
    print("Acumular millas")

    opcion=0
    while opcion!=4:
        print("__MENU__")
        print("1-Consultar millas \n2-Acumular millas \n3- Canjear millas \n4- Salir menu")
        opcion=int(input("Ingrese la opcion que desea realizar"))
        if opcion==1:
            print("La cantidad total de millas es {}".format(viajeroNuevo.cantidadYotaldeMillas()))
        if opcion==2:
            cant=int(input("Ingrese la cantidad de millas a acumular"))
            viajeroNuevo.acumularMillas(cant)
            print("La cantitad todtal de millas se actualizo {}>>".format(viajeroNuevo.cantidadYotaldeMillas()))
        if opcion==3:
            canjear=int(input("ingrese las millas a canjear"))
            f=viajeroNuevo.canjearMillas(canjear)
            if f==True:
                print("La cantitad todtal de millas se actualizo {}>>".format(viajeroNuevo.cantidadYotaldeMillas())) 

            


    

    
    
    