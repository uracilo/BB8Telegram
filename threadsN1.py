import threading
def funcion():
    print('Aldo es mi adjunto favorito :3')

hilos = []#Creamos una lista de hilos vacía por el momento

for i in range(11):
    hilos.append(threading.Thread(target=funcion))
    #En cada iteración agregamos un hilo a la lista
    #con el bloque ejecutable funcion a llamar en cada hilo
    hilos[i].start()
