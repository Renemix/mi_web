def menuPP(opMenu):
    while opMenu != "4":
        print()
        print("Seleccione el club de futbol.\n1.Boca Juniors\n2.River Plate\n3.Independiente")
        opMenu = input("Ingrese la opción: ")
        if opMenu == "1":
            BocaJuniors()
        elif opMenu == "2":
            RiverPlate()
        else:
            Independiente()
        break

        
def BocaJuniors():
    print("Boca Juniors tiene 6 libertadores")
    
def RiverPlate():
    print("River Plate tiene 4 libertadores")
    
def Independiente():
    print("Independiente tiene 7 libertadores")

opMenu= ""
menuPP(opMenu)