#22 Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc

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

def mcu(cola: Queue) -> None:
    capitana_marvel = None
    superheroes_femeninos = []
    personajes_masculinos = []
    scott_lang = None
    datos_con_s = []
    carol_danvers_esta = False
    carol_danvers = None

    #a. nombre de capitana marvel 
    for _ in range(cola.size()):
        actual = cola.on_front()
        if actual['superheroe'] == 'Capitana Marvel':
            capitana_marvel = actual['personaje']
            
        # b. Mostrar los nombres de los superheroes femeninos
        if actual['genero'] == 'F':
            superheroes_femeninos.append(actual['superheroe'])
            
        # c. Mostrar los nombres de los personajes masculinos
        if actual['genero'] == 'M':
            personajes_masculinos.append(actual['personaje'])
            
        # d. Determinar el nombre del superhéroe del personaje Scott Lang
        if actual['personaje'] == 'Scott Lang':
            scott_lang = actual['superheroe']
            
        # e. Mostrar todos los datos si el nombre empieza con 'S'
        if actual['personaje'].startswith('S') or actual['superheroe'].startswith('S'):
            datos_con_s.append(actual)
            
        # f. Determinar si Carol Danvers está y cuál es su superhéroe
        if actual['personaje'] == 'Carol Danvers':
            carol_danvers_esta = True
            carol_danvers = actual['superheroe']
            cola.move_to_end()

    print(f"a. Personaje de Capitana Marvel: {capitana_marvel}")
    print(f"b. Superhéroes femeninos: {', '.join(superheroes_femeninos)}")
    print(f"c. Personajes masculinos: {', '.join(personajes_masculinos)}")
    print(f"d. Superhéroe de Scott Lang: {scott_lang}")
    print("e. Personajes/Superhéroes que comienzan con 'S':")
    for dato in datos_con_s:
        print(f"   - {dato}")
    if carol_danvers_esta:
        print(f"f. Carol Danvers sí se encuentra en la cola. Su superhéroe es: {carol_danvers}")
    else:
        print("f. Carol Danvers NO se encuentra en la cola.")
mcu_cola = Queue()

mcu_cola.arrive({'personaje': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'})
mcu_cola.arrive({'personaje': 'Steve Rogers', 'superheroe': 'Capitán América', 'genero': 'M'})
mcu_cola.arrive({'personaje': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'})
mcu_cola.arrive({'personaje': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'})
mcu_cola.arrive({'personaje': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'})
mcu_cola.arrive({'personaje': 'Wanda Maximoff', 'superheroe': 'Scarlet Witch', 'genero': 'F'})
mcu_cola.arrive({'personaje': 'Peter Parker', 'superheroe': 'Spider-Man', 'genero': 'M'})

mcu(mcu_cola)
print(f"\n[Verificación] Tamaño final de la cola: {mcu_cola.size()} (¡No se perdió ningún dato!)")