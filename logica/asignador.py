class Asignador_voraz:
    def __init__(self, camion, bodega):
        self.camion = camion
        self.bodega = bodega
        
    def asignar(self):
        # Ordenar los elementos por valor/peso en orden descendente
        elementos = sorted(self.bodega.elementos, key=lambda e: e.peso, reverse=True)
        
        for elementos in elementos:
            camion_destino = min(self.camion, key=lambda c: c.peso)
            camion_destino.agregar_elemento(elementos)
        self.bodega.elemento=[]
        

