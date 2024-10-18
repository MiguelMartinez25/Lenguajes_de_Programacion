class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ProductModel:
    def __init__(self):
        self.catalog = []
        self.observers = []  # Lista de observadores

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update()  # Notificar a los observadores

    def addProduct(self, product: Product):
        self.catalog.append(product)
        self.notifyObservers()  # Notificar a los observadores cuando se añade un producto

    def getCatalog(self):
        return self.catalog
