class Employee:
    
    #atributos de clase ("static" en java)
    headquarters = "Cali"
    
    #método de inicialización ("constructor")
    def __init__(self, name, salary):
        #atributos de self (this) son atributos de instancia
        #"self" hace referencia a la instancia y es simepre
        #el primer parámetro de los métodos de objeto:
        self.name = name
        self.salary = salary
        
    def calculatePayroll(self):
        return self.salary * 0.85
    
    def save_to_db(self):
        print("saving salary = {self.salary} to database")
          
#Implemetación después de SRP:
#Clase "Modelo"
class Employee_Model:
    
    headquarters = "Cali"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
class Employee_Controller:
    pass

class Employee_Persistence:
    def save_to_db(self, employee):
        print(f"Saving {employee.name} {employee.salary} to db")
        
#2. Open/Closed Principle (OCP)
#antes de aplicar el principio:

class PartTimeEmployee(Employee):
    def PayrollCalculator(self):
        return "salario para empleado medio tiempo"

class FullTimeEmployee(Employee):
    def PayrollCalculator(self):
        return "salario para empleado tiempo completo"

class InternEmployee(Employee):
    def PayrollCalculator(self):
        return "salario para empleado practicante"
    
#después de aplicar el principio:
#aplicación de patrón de diseño "strategy":
        
class PayrollStrategy:
    def PayrollCalculator(self, employees):
        for e in employees:
            print(e.PayrollCalculator())
            

#3. Liskov Substitution Principle:
#Definition: Las clases derivadas deben poder sustituir a sus clases base
#sin alterar el comportamiento esperado del programa

#Ejercicio: -Implementar principios S, O (abierto y cerrado, responsabilidad única) 2 ejemplos.
#-Ejemplo de principio L (LSP) definición. (uso de ABC Abstract Base Clases)