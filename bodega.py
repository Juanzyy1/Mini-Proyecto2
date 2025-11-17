class Bodega:
    def __init__(self):
        self.elementos = []
        
    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)
        
        
    def quitar_elemento(self, elemento):
        self.elementos.remove(elemento)
        
        