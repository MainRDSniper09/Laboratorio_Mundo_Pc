from Computadora import Computadora  # Se importa la clase Computadora


class Orden:  # Se crea la clase Orden
    contador_ordenes = 0  # Se inicializa el contador en 0 para el ID orden

    def __init__(self, computadoras):  # Se instacia el atributo computadora para crear una lista
        Orden.contador_ordenes += 1  # Se incrementa el contador en 1
        self.id_orden = Orden.contador_ordenes  # Se le asigna el valor de Contador_ordenes a 'id_orden'
        self._computadoras = list(computadoras)  # Se crea la lista computadoras

    def agregar_computadora(self, computadora):  # Se crea la funcion agregar computadora en donde recibe de parametro 'computadora'
        self._computadoras.append(computadora)  # Se usa el atributo '_computadora' y se usa la funcion 'append' para agregar a la lista computadora creada anteriormente

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:  # Se crea un ciclo for para que recorra la lista y vaya agregando sus respectivos datos
            computadoras_str += computadora.__str__() + ' | '  # Se realiza una concatenacion del simbolo '|' para que lo ponga al final de cada Computadora creada

        return f'Orden {self.id_orden}: {computadoras_str}'  # Se realiza el respectivo __str__ para imprimir los datos tanto el ID de la orden y todo el objeto computadora


if __name__ == '__main__':  # Prueba realizada anterior mente, funcionando a la perfecccion
    computadora1 = Computadora('Pc Gamer', '48 pulgadas', 'MSI', 'Bluetooth', 'SnapDragon', 'USB', 'MSI')
    computadora2 = Computadora('Workstation', '32 pulgadas', 'Dell', 'USB-C', 'Logitech', 'USB', 'HP')

    ordenUno = Orden([computadora1, computadora2])
    print(ordenUno)

    ordenUno.agregar_computadora(Computadora('Laptop', '15 pulgadas', 'HP', 'Wireless', 'HP', 'Wireless', 'HP'))
    print(ordenUno)
