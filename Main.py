from Model import *
from View import *
from Controller import *

def main():
    # Instanciar objetos de MVC:
    myModel = ProductModel()
    myView = ProductView()
    myController = ProductCatalogController(myModel, myView)
    
    # Imprimir opciones:
    print("Menu\n")
    print("1. Adicionar Producto ")
    print("2. Mostrar Catálogo ")
    print("3. Salir ")
    
    while True:
        # Manejar opciones:
        sel = int(input("Seleccione una opción: "))
        if sel == 1:
            myController.addNewProduct()
        elif sel == 2:
            myController.showProducts()
        elif sel == 3:
            break  # Salir del bucle
        else:
            print("Opción no válida")
        
if __name__ == "__main__":
    main()
