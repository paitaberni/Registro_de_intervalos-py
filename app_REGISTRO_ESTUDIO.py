









import datetime as dt
import json

if __name__ == '__main__':

    intervalos_lista = []

    def crear_intervalo():
        n = len(intervalos_lista)
        intervalo = {
            "id": n,
            "inicio": dt.datetime.today(),
            "final": None, # final del intervalo,
            "duracion": None,# duracion del intervalo,
        }
        print("Se ha creado un intervalo: "+ str(intervalos_lista[n]))
        return intervalo
    def cerrar_intervalo(n):
        intervalo = intervalos_lista[int(n)]
        intervalo["final"] = dt.datetime.today()
        intervalo["duracion"] = intervalo["final"] - intervalo["inicio"]
        print("se ha modificado un intervalo: "+ str(intervalo))
    while True:
        x = input("Que quieres hacer?\n Iniciar un intervalo..........I \n Finalizar un intervalo..........F \n cerrar el programa.........x  ").lower()
        if x == "i":
            crear_intervalo()
        elif x == "f":
            k = input("\n¿que intervalo quieres terminar?\n")
            cerrar_intervalo(k)
        elif x == "x": quit()
        else: print("\n Escriba para elegir una opción." )

