class Camion:
    def __init__(self, placa:str, modelo:str, marca:str):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.carga = []
        self.peso = 0
        self.valor = 0
        
        
    def agregar_elemento(self, elemento):
        self.carga.append(elemento)
        self.peso += elemento.peso
        self.valor += elemento.valor
        
    def __repr__(self):
        return f"Camion(placa={self.placa} ({self.marca}-{self.modelo})"
        
        
    
        