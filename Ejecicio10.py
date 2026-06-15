#10 Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades

from typing import Any

class Queue:
    def __init__(self):
        self.__elements = []
    def arrive(self, value: Any) -> None: 
        self.__elements.append(value)
    def attention(self) -> Any:
        return self.__elements.pop(0)
    def size(self) -> int:
        return len(self.__elements)
    def on_front(self) -> Any:
        return self.__elements[0]
    def move_to_end(self) -> Any:
        value = self.__elements.pop(0)
        self.__elements.append(value)
        return value

class Stack:
    def __init__(self):
        self.__elements = []
    def push(self, value: Any) -> None:
        self.__elements.append(value)
    def pop(self) -> Any:
        return self.__elements.pop()
    def size(self) -> int:
        return len(self.__elements)
    
#a eliminar las notificaciones de facebook
def eliminar(cola: Queue) -> None:
    for _ in range(cola.size()):
        notificacion = cola.on_front()
        if notificacion['app'] == "facebook":
            cola.attention()  
        else:
            cola.move_to_end() 

#b mostrar notificaciones de twitter que incluyan python
def twitter(cola: Queue) -> None:
    print("--- Notificaciones de twitter sobre python ---")
    for _ in range(cola.size()):
        notificacion = cola.on_front()
        if notificacion['app'] == 'Twitter' and 'Python' in notificacion['mensaje']:
            print(f"[{notificacion['hora']}] {notificacion['mensaje']}")
        cola.move_to_end() 

#c notificaciones entre 11:43 y 15:57
def contar_notificaciones(cola: Queue) -> int:
    pila_temporal = Stack()
    for _ in range(cola.size()):
        notificacion = cola.on_front()
        if "11:43" <= notificacion['hora'] <= "15:57":
            pila_temporal.push(notificacion)
        cola.move_to_end() 
    cantidad = 0
    while pila_temporal.size() > 0:
        pila_temporal.pop() # Sacamos de la pila
        cantidad += 1
    return cantidad

mi_cola = Queue()
mi_cola.arrive({'hora': '10:30', 'app': 'WhatsApp', 'mensaje': "hola"})
mi_cola.arrive({'hora': '11:50', 'app': 'Facebook', 'mensaje': 'Tienes una solicitud de amistad'}) 
mi_cola.arrive({'hora': '12:15', 'app': 'Twitter', 'mensaje': 'Nuevo tutorial de Python disponible'}) 
mi_cola.arrive({'hora': '14:00', 'app': 'Facebook', 'mensaje': 'A Juan le gusta tu foto'}) 
mi_cola.arrive({'hora': '16:10', 'app': 'Twitter', 'mensaje': 'Aprende a programar en Python hoy'}) 

print(f"Tamaño inicial de la cola: {mi_cola.size()}")
eliminar(mi_cola)
print(f"Tamaño después de borrar Facebook: {mi_cola.size()}") # Debería ser 3
twitter(mi_cola) 

cantidad_rango = contar_notificaciones(mi_cola)
print(f"Notificaciones recibidas entre 11:43 y 15:57: {cantidad_rango}")