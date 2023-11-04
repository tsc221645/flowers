#--------------------------------
# FLOWERS
# Author: tsc221645
# Date: 11/03/2023
#-------------------------------


def menuPrincipal():
    print("Bienvenido!\n")
    op = 0
    while(op < 1 or op > 6): 
        print("Selecciona la opcion del menu")
        print("1. Girasol\n2. Lavanda\n3. Rosa\n4.Tulipan\n5.Ramo\n6.Salir")
        if(op == 1):
            print("Usted ha seleccionado un girasol")
