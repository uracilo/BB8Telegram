import threading
import time

condicion = threading.Condition()
listo = False

class Persona(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global listo
        condicion.acquire()
        while not listo:
            print('[%s] Deja que caliente el coche...' % time.strftime('%H:%M:%S'))
            condicion.wait()

        print('[%s] \'Amonos!' % time.strftime('%H:%M:%S'))
        condicion.notify()
        condicion.release()

class Auto(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global listo
        condicion.acquire()
        for i in range(3):
            time.sleep(1)

        print('[%s] El coche ya calentó' % time.strftime('%H:%M:%S'))
        listo = True
        condicion.notify()
        condicion.release()

persona = Persona()
auto = Auto()

persona.start()
auto.start()

persona.join()
auto.join()


"""Cuando llamamos a start está realizando la tarea que está en run de cada clase

La persona tomará el bloqueo de la condición, pero como el coche no etá listo
esperará, llamando a wait() se libera ese bloqueo temporalmente esto hará que el
hilo de la clase Auto tome el mando, así espera 3 segundos y libera el bloqueo
despues indica que está listo cambiando el valor de la variable listo a True

el join del final es para que el hilo principal espere a que terminen los otros hilos


"""
