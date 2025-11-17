class Asignador_voraz:
    def __init__(self):
        pass
    
    def asignar(self, bodega, camiones):
        # Ordenar los elementos por valor/peso en orden descendente
        elementos = sorted(bodega.elementos, key=lambda e: e.peso, reverse=True)
        
        for elemento in elementos:
            camion_destino = min(camiones, key=lambda c: c.peso)
            camion_destino.agregar_elemento(elemento)
        bodega.elementos=[]
        

