from Computadora import Computadora
from Orden import Orden

computadora1 = Computadora('Pc Gamer', '48 pulgadas', 'MSI', 'Bluetooth', 'SnapDragon', 'USB', 'MSI')
computadora2 = Computadora('Workstation', '32 pulgadas', 'Dell', 'USB-C', 'Logitech', 'USB', 'HP')

ordenUno = Orden([computadora1, computadora2])  # Se crea el objeto ordenUno en la cual se crea como una lista, respectivamente para recibir los datos del objeto computadora1 y computadora2
print(ordenUno)  # Se imprime esta lista

ordenUno.agregar_computadora(Computadora('Laptop', '15 pulgadas', 'HP', 'Wireless', 'HP', 'Wireless', 'HP'))  # Se manada a llamar la funcion 'agregar_computadora' para agregar otra computadora y ver que todo funcione correctamente
print(ordenUno)  # Se imprime la nueva ordenUno con un nuevo objeto tipo Computadora
