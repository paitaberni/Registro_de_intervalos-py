









import datetime as dt
import json
from operator import index
from typing import final


def leer_lista():
    with open("Lista_Intervalos.json", "r") as f:
        lista_intervalos = json.load(f)
        for intervalo in lista_intervalos:
            print(str(intervalo))
            IntervaloDeTiempo.crear_intervalo(**intervalo)

    return


class  IntervaloDeTiempo:

    raiz = []
    intervalos = []
    def __init__(self, id, inicio, final, delta):
        self.inicio = inicio
        self.final = final
        self.delta = delta
        self.id = id



    def crear_intervalo(**kwargs):
        ##n = len(intervalos_lista)

        if not kwargs:
            id = input("Ponle un nombre: ")
            inicio = dt.datetime.today().isoformat(timespec="seconds")
            nuevo = IntervaloDeTiempo(id, inicio, None, None)
        else:
            id = kwargs["id"]
            inicio = kwargs["inicio"]
            final = kwargs["final"]
            delta = kwargs["delta"]
            nuevo = IntervaloDeTiempo(id, inicio, final, delta)

        IntervaloDeTiempo.intervalos.append(nuevo)
        print("Se ha creado un intervalo: " + "\n" + id + "\n" + inicio)
        return

    @staticmethod
    def cerrar_intervalo():
        # lista_intervalos = leer_lista()
        print("Elige un intervalo para cerrar:\n")
        for i in range(len(IntervaloDeTiempo.intervalos)):
            print(str(i+1) +"." + IntervaloDeTiempo.intervalos[i].id)
            print(str(IntervaloDeTiempo.intervalos[i].inicio) + "\n")
        indice = int(input("Ingrese el numero del intervalo:\n ")) - 1
        intervalo_seleccionado = IntervaloDeTiempo.intervalos[indice]
        intervalo_seleccionado.final = dt.datetime.today()
        inicio = dt.datetime.fromisoformat(intervalo_seleccionado.inicio)

        intervalo_seleccionado.delta = intervalo_seleccionado.final - inicio
        intervalo_seleccionado.delta = int(intervalo_seleccionado.delta.total_seconds())
        print("se ha modificado un intervalo: " + str(intervalo_seleccionado.id))
        intervalo_seleccionado.final = intervalo_seleccionado.final.isoformat(timespec="seconds")
        IntervaloDeTiempo.intervalos[indice] = intervalo_seleccionado
        # guardar_lista(lista_intervalos)
        return
    def to_dict(self):
        diccionario = {
            "id": self.id,
            "inicio" : self.inicio,
            "final" : self.final,
            "delta" : self.delta,
        }
        return diccionario

    # def guardar_lista(intervalos_lista):
    #     with open("Lista_Intervalos.json", "w") as k:
    #         json.dump(intervalos_lista , k, indent=4, ensure_ascii=False)
    #     return


def cerrar():
    json_data = []
    for intervalo in IntervaloDeTiempo.intervalos:
        json_data.append(intervalo.to_dict())

    print(str(IntervaloDeTiempo.intervalos))
    with open("Lista_Intervalos.json", "w") as k:
      json.dump(json_data , k, indent=4, ensure_ascii=False)
    return


if __name__ == '__main__':
    leer_lista()
    while True:
        x = input("Que quieres hacer?\n Iniciar un intervalo..........I \n Finalizar un intervalo..........F \n cerrar el programa.........x  ").lower()
        if x == "i":
            IntervaloDeTiempo.crear_intervalo()
        elif x == "f":
            IntervaloDeTiempo.cerrar_intervalo()
        elif x == "x":
            cerrar()
            break

        else: print("\n Escriba para elegir una opción." )

