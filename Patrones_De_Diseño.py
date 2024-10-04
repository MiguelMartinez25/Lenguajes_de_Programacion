#1. CREATIONAL PATTERNS: Se centran en cómo son creados los objetos en un módulo de software
#1.a. Singleton: Solo se admite una instancia de 1 objeto en un módulo de software

class NotSingleton():
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
notSingleton1 = NotSingleton("Diego", "abcd1234")
notSingleton2 = NotSingleton("Diana", "efgh5678")
#notSingleton1 y notSingleton2
print(notSingleton1 is notSingleton2)


class Singleton():
    #atributo de la clase para la instancia de clase
    #(inicialmente es None, no Null)
    _instance = None
    
    
    #método de instanciación de clase:
    def __new__(self):
        #valida que no se haya creado una instancia antes:
        if self._instance is None:
            #crea una instancia como objeto genérico de python
            self._instance = super(Singleton, self).__new__(self)
            #atributo de instancia, de ejemplo
            self._instance.config = {}

objeto1 = Singleton()
objeto2 = Singleton()            

print("Funciona el uso del singleton?: ")
print(objeto1)
print(objeto2)
print(objeto1 is objeto2)

#Ejemplo de aplicación:
#Un objeto de conexión a base de datos que se comporta como un singleton
#solo se admite una instancia de la clase DatabaseCOnnection en un módulo
#USO: Administración de recursos compartidos: configuraciones globales, recursos limitados, etc
class DatabaseConnection(Singleton):
    
    def __init__(self):
        if "connection_string" not in self.config:
            self.config["connection_string"] = this.connectToDatabase()
    
    def connectToDatabase(self):
        return "sample connection string"
    
connection1 = DatabaseConnection()
connection2 = DatabaseConnection()
print(f"son la misma conexión? {connection1 is connection2}")
