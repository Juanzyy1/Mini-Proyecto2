from logica.asignador import Asignador_voraz
from elemento import Elemento
from bodega import Bodega
from camion import Camion

def main():
    # Crear una bodega y agregar elementos
    bodega = Bodega()
    bodega.agregar_elemento(Elemento("E01", "Elemento1", 10, 100))
    bodega.agregar_elemento(Elemento("E02", "Elemento2", 20, 150))
    bodega.agregar_elemento(Elemento("E03", "Elemento3", 15, 120))
    
    # Crear camiones
    camion1 = Camion(placa="ABC123", modelo="2020", marca="MarcaA")
    camion2 = Camion(placa="DEF456", modelo="2019", marca="MarcaB")
    camiones = [camion1, camion2]
    
    # Asignar elementos a los camiones usando el asignador voraz
    asignador = Asignador_voraz()
    asignador.asignar(bodega, camiones)
    
    # Mostrar el contenido de los camiones después de la asignación
    for camion in camiones:
        print("\n", camion)
        for elemento in camion.carga:
            print(f"  - {elemento.codigo}:{elemento.nombre}, Peso: {elemento.peso}, Valor: {elemento.valor}")
            
if main():
    main()