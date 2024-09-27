#Definición principio L: Las clases derivadas deben poder sustituir a sus clases base
#sin alterar el comportamiento esperado del programa
#No aplicación del principio L:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def payCalculator(self, factor):
        self.salary = self.salary * factor
        return self.salary

class Contractor(Employee):
    
    def payCalculator(self, factor):
        #return super().payCalculator(factor)
        raise NotImplementedError("el método en la subclase no está implementado")

#Aplicación correcta del principio L:

class FullTimeEmployee(Employee):
    
    def payCalculator(self, factor):
        #Implementación de la propia lógica del método en la subclase:
        return super().payCalculator(factor)
    
#----------------------------------------------------------------------------------------------------------------------    
#Principio de segregación de interface (Interface Segregation Principle): Principio de segregación de interfaces
# (a) No se deben tener clases que implementen métodos que no se usan
# (b) No se deben tener clases que dependan de interfaces que no se usan
# (c) Evitar tener interfaces muy grandes con comportamientos/funciones que algunas clases no exhiban/implementen
 
#Superclase
class Worker:
    def work(self):
        pass
    
    def commute(self):
        pass

#Subclases:
class RemoteWorker(Worker):
    def work(self):
        print("Working remote")
    
    #Implementar este método vulnera el principio:
    #¿Cómo se aplica?
    #Solución 1: no implementar la función que no se va a usar
    #Solución 2: separar el comportamiento en dos interfaces: una tiene el contrato de "commute" y la otra no
    #def commute(self):
    #    raise NotImplementedError("remote workers doesn't commute")
    
class OfficeWorker(Worker):
    def work(self):
        print("Working from office")
        
    def commute(self):
        print("Commuting to office...")
    
#----------------------------------------------------------------------------------------------------------------------
#Principio Inversión de Dependencia (Dependency Inversion Principle)
# (1) Los módulos de alto nivel no deben depender de los módulos de bajo nivel: deben depender solo de abstracciones (interfaces)
# La solución 2 del ejemplo anterior implementa este principio