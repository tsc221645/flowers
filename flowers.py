#--------------------------------
# FLOWERS
# Author: tsc221645
# Date: 11/03/2023
#-------------------------------
import girasol as g
import lavanda as l
import rosa as r
import tulipan as tuli

def menuPrincipal():
    print("Bienvenido!\n")
    op = 0
    while(op < 1 or op > 6): 
        print("Selecciona la opcion del menu")
        print("1. Girasol\n2. Lavanda\n3. Rosa\n4. Tulipan\n5. Ramo\n6. Salir")
        op = int(input("Ingrese la opcion: "))
        if(op == 1):
            print("Usted ha seleccionado un girasol")
        elif(op == 2):
            print("Usted ha seleccionado una lavanda")
        elif(op == 3):
            print("Usted ha seleccionado una rosa")
        elif(op == 4):
            print("Usted ha seleccionado una tulipan")
        elif(op == 5):
            print("Usted ha seleccionado una ramo")
        elif(op == 6):
            print("Saliendo....")
            exit()

menuPrincipal()