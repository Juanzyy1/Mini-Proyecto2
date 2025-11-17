class Elemento:
    def __init__(self, codigo, nombre, peso, valor):
        self.codigo = codigo
        self.nombre = nombre
        self.peso = peso
        self.valor = valor
        
    def __repr__(self):
        return f"{self.codigo}-{self.nombre} (Peso: {self.peso}, Valor: {self.valor})"