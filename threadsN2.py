import threading

indice = 1

def funcion():
    global indice
    print('Aldo es mi adjunto favorito :3 x%i, hilo: %s' % (indice, threading.current_thread().ident))
    indice += 1

hilos = []
for i in range(11):
    hilos.append(threading.Thread(target=funcion))
    hilos[i].start()
