# BEHAVIORAL PATTERNS
# OBSERVER: permite que obejtos se suscriban a los cambios o eventos generados 
# por otros objetos
"""
class Subject:
    def __init__(this):
        this._observers = []
        
    def attach(this, observer):
        this._observers.append(observer)
    
    def attach(this, observer):
        this._observers.remove(observer)
    
    def attach(self, message):
        for observer in observer:
            observer.update(message)

#observador generico:            
class Observer():
    def update(this, message):
        #implementar manejo del mensaje
        pass
    
#observador concreto:
class ConcreteObserver(Observer):
    def update(this, message):
        print(f"El observador recibio el {message}")

#emisor        
subject = Subject()

#subscriptores:
obs1 = ConcreteObserver()
obs2 = ConcreteObserver()

#suscribir:
subject.attach(obs1)
subject.attach(obs2)

subject.notify(">>Mensaje a todos los subscriptores")
"""
# 3. STRUCTURAL PATTERNS
# ADAPATER: "adapta" la interfaz de un objeto a la que pueda entender a otro objeto
#               permite que objetos con interfaces incompatibles puedan colaborar

#interfaz destino:
class Target:
    def request(this):
        return "comportamiento por defecto del target..."

#interfaz que no es compatible
class Adaptee:
    def specific_request(this):
        return "contenido incompatible"

#clase adaptadora:
class Adapter(Target):
    
    def __init__(this, adaptee: Adaptee):
        this._adaptee = adaptee

    def request(this):
        #return this._adaptee.specific_request()
        return f"contenido adaptado alo que el cliente requiere:{this._adaptee.specific_request()}"

def client(target: Target):
    print(target.request())

#trabaja con el target:
new_target = Target()
client(new_target)

#creamos instancia de la clase con interfaz incompatible:
clase_adaptada= Adapter()
print(f"Llamado a método no compatible {clase_adaptada.specific_request()}")

#se llama el request específico a través del adaptor:
nuevo_adapter = Adapter()
client(nuevo_adapter)

