from Model import *
from View import *

class ProductCatalogController:
    def __init__(self, model: ProductModel, view: ProductView):
        self.model = model
        self.view = view
        self.model.addObserver(self)  # Registrarse como observador

    def update(self):
        # Actualizar la vista o realizar otra acción cuando se añade un producto
        self.showProducts()  # Mostrar el catálogo actualizado

    def addNewProduct(self):
        name, price = self.view.addNewProduct()
        newProduct = Product(name, price)
        self.model.addProduct(newProduct)  # Añadir producto al modelo

    def showProducts(self):
        catalog = self.model.getCatalog()
        self.view.displayCatalog(catalog)
