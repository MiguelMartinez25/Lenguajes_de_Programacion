class ProductView:
    
    def displayCatalog(self, products):
        if products:
            print("Lista de productos\n")
            for p in products:
                print(f"Producto {p.name}, precio: {p.price}")
        else:
            print("El catálogo está vacío")

    def addNewProduct(self):
        name = input("Ingrese el nombre del nuevo producto: ")
        price = input("Ingrese el precio del nuevo producto: ")
        return name, price
