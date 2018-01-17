import threading
import time

N = 8
sem = threading.Semaphore(3)

class MiHilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id


    def run(self):
        sem.acquire()
        print('Hilo %d en la hora %s' % (self.id, time.strftime('%H:%M:%S')))
        time.sleep(self.id+2)
        sem.release()

hilos = []

for n in range(N):
    actual = MiHilo(n+1)
    hilos.append(actual)
    actual.start()

for actual in hilos:
    actual.join()

"""Ejecutando este código vemos que los primeros tres hilos se ejecutan a la vez
pero luego comienzan a ejecutarse a horas distintas, si todos tuvieran un sleep identico
se irían ejecutando de 3 en 3"""
