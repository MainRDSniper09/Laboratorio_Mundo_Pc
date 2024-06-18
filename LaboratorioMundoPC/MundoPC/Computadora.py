from DispositivoEntrada import Raton, Teclado
from Monitor import Monitor

'''
    Se importan las librerias respectivas para poder crear un objeto computadora completo
'''

class Computadora:  # Se crea la clase computadora
    contador_computadoras = 0  # Se crea un contador de ID computadoras

    def __init__(self, nombre, tamanio_monitor, marca_monitor, tipo_entrada_raton, marca_raton, tipo_entrada_teclado, marca_teclado):  # Se inicializan los atributos respectivos para que pueda recibir los parametros correspondientes
        Computadora.contador_computadoras += 1  # Se incrementa en 1 el contador de ID computadoras
        self.__id_computadora = Computadora.contador_computadoras  # Se le asigna el valor del contador a '__id_computadora'
        self.__nombre = nombre

        self.monitor = Monitor(marca_monitor, tamanio_monitor)  # Se crea el atributo monitor que recibe los parametros instanciados anteriormente
        self.raton = Raton(tipo_entrada_raton, marca_raton)  # Se crea el atributo raton que recibe los parametros instanciados anteriormente
        self.teclado = Teclado(tipo_entrada_teclado, marca_teclado)  # Se crea el teclado monitor que recibe los parametros instanciados anteriormente

    def __str__(self):
        return (f'Computadora [ID: {self.__id_computadora}, Nombre: {self.__nombre}, '
                f'{self.monitor}, {self.raton}, {self.teclado}]')  # Se crea el __str__ el cual va a imprimir los datos tanto de computadora, raton, teclado y monitor
