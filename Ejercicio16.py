#16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la siguiente situación

from typing import Any

class PriorityQueue:
    def __init__(self):
        self.__elements = []

    def arrive(self, documento: str, prioridad: int) -> None:
        self.__elements.append({'documento': documento, 'prioridad': prioridad})
        self.__elements.sort(key=lambda x: x['prioridad'], reverse=True)

    def attention(self) -> str:
        if self.size() > 0:
            return self.__elements.pop(0)['documento']
        return "la cola de impresion está vacia."

    def size(self) -> int:
        return len(self.__elements)
    
cola_impresion = PriorityQueue()

# a Cargue tres documentos de empleados (Prioridad 1)
cola_impresion.arrive("Recibo_Sueldo_Emp1", 1)
cola_impresion.arrive("Recibo_Sueldo_Emp2", 1)
cola_impresion.arrive("Recibo_Sueldo_Emp3", 1)

# b Imprima el primer documento de la cola
print("\n Imprimiendo primer documento:")
print(f" -> {cola_impresion.attention()}") 

# c. Cargue dos documentos del staff de TI (Prioridad 2)
cola_impresion.arrive("Reporte_Servidores_TI", 2)
cola_impresion.arrive("Inventario_Equipos_TI", 2)

# d Cargue un documento del gerente (Prioridad 3)
cola_impresion.arrive("Balance_General_Gerente", 3)

# e Imprima los dos primeros documentos de la cola
print("\ne. Imprimiendo los dos primeros documentos actuales:")
print(f" -> {cola_impresion.attention()}") 
print(f" -> {cola_impresion.attention()}") 

# f Cargue dos documentos de empleados (1) y uno de gerente (3)
cola_impresion.arrive("Solicitud_Vacaciones_Emp4", 1)
cola_impresion.arrive("Justificativo_Medico_Emp5", 1)
cola_impresion.arrive("Contratos_Nuevos_Gerente", 3)

# g Imprima todos los documentos restantes de la cola de impresión
print("\ng. Imprimiendo todos los documentos restantes en orden de prioridad:")
while cola_impresion.size() > 0:
    print(f" -> {cola_impresion.attention()}")