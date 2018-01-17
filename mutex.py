import threading

mutex = threading.Lock()
indice = 1

def funcion():
    global indice
    mutex.acquire()
    print('Aldo es mi adjunto favorito :3 x%i' % indice)
    indice += 1
    mutex.release()

hilos = []
for i in range(11):
    hilos.append(threading.Thread(target=funcion))
    hilos[i].start()
