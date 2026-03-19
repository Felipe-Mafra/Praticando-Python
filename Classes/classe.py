class Carro: 
    lista_carros = []

    def __init__(self, nome, placa, marca):
        self._nome = nome
        self.placa = placa
        self.marca = marca
        self._estoque = False
        Carro.lista_carros.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self.placa} | {self.marca}'
    
    @classmethod
    def printar_carros(cls):
        print(f'{'Nome do Carro'.ljust(25)} | {'Placa do Carro'.ljust(25)} | {'Marca'.ljust(25)} | {'Status'}')
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        for veiculo in cls.lista_carros:
            print(f'{veiculo._nome.ljust(25)} | {veiculo.placa.ljust(25)} | {veiculo.marca.ljust(25)} | {veiculo.estoque} ')
    @property
    def estoque(self):
        return 'Veiculo no estoque' if self._estoque else 'Indisponivel no estoque'
    
    def alternar_estado(self):
        self._estoque = not self._estoque
    
c1 = Carro('voyage', 'pui1553', 'VW')
c2 = Carro('space fox','pwb7337','VW')
c2.alternar_estado()

Carro.printar_carros()