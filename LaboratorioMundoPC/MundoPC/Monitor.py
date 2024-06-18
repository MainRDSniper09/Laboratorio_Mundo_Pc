# Monitor.py
class Monitor:  # Se crea la clase Monitor
    contador_monitores = 0  # Se crea un contador para el ID monitor

    def __init__(self, marca, tamanio):  # Se crea los atributos para recibir los parametros del monitor
        Monitor.contador_monitores += 1  # Se le incrementa al contador en 1 para el ID monitor
        self.__id_monitor = Monitor.contador_monitores  # Se le asigna el valor de Contador monitores a '__id_monitor'
        self.__marca = marca
        self.__tamanio = tamanio

    @property
    def id_monitor(self):
        return self.__id_monitor

    @property
    def tamanio(self):
        return self.__tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio

        '''
        Se crean los respectivos Getters and Setters
        '''

    def __str__(self):
        return f'Id Monitor: {self.id_monitor}, Marca: {self.__marca}, Tamaño: {self.__tamanio}'  # Se realiza el __str__ para imprimir los datos del monitor
