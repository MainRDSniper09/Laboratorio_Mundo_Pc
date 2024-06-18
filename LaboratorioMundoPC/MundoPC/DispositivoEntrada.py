# DispositivoEntrada.py
class DispositivoEntrada:  # Se crea la clase padre
    def __init__(self, tipo_entrada, marca):  # Se inicializa los objetos a recibir
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    @property
    def tipo_entrada(self):
        return self._tipo_entrada

    @property
    def marca(self):
        return self._marca

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    '''
    Se crean Getters and Setters
    '''

    def __str__(self):
        return f'Tipo de entrada: {self.tipo_entrada}, Marca: {self.marca}'  # Se manda a imprimir el tipo de entrada y la marca del dispositivo

# Raton.py
class Raton(DispositivoEntrada):  # Se crea la clase raton 'Heredada de la clase Dispositivo Entrada'
    contador_ratones = 0  # Se crea un contador de Ratones

    def __init__(self, tipo_entrada, marca):  # Se inicializa los objetos a recibir
        Raton.contador_ratones += 1  # Se realiza un incremento para generar el ID UNICO para el raton
        self.__id_raton = Raton.contador_ratones  # Se le asigna el valor del contador a '__id_raton'
        super().__init__(tipo_entrada, marca)  # Se hereda los atributos de la clase padre

    @property
    def id_raton(self):  # Se crea el respectivo Get de nuestro atributo
        return self.__id_raton

    def __str__(self):
        return f'Id Raton: {self.id_raton}, {super().__str__()}'  # Se realiza el ToString para imprimir el Id del raton y se hereda el __str__ de la clase padre para concatenarlo

# Teclado.py
class Teclado(DispositivoEntrada):  # Se crea la clase Teclado que hereda tambien de la clase padre
    contador_teclados = 0  # Se crea un contador de ID para los teclados

    def __init__(self, tipo_entrada, marca):  # Se inicializan los objetos
        Teclado.contador_teclados += 1   # Se incrementa el contador de teclados
        self.__id_teclado = Teclado.contador_teclados  # Se le asigna el valor del contaor a '__id_telado'
        super().__init__(tipo_entrada, marca)  # Se hereda los atributos de la clase padre

    @property
    def id_teclado(self):  # Se hace el respectivo Get de 'id_teclado'
        return self.__id_teclado

    def __str__(self):
        return f'Id Teclado: {self.id_teclado}, {super().__str__()}'  # Se realiza el __str__ para imprimir el Id Teclado y heredamos el __str__ de la clase padre para imprimir los demas detalles
