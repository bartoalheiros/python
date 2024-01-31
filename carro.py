"""
Introducao a Orientacao a Objetos:
Acesso de atributos e metodos 
"""
class Carro:
    #inicializar o objeto
    def __init__(self, v_inicial=5):
        self.__velocidade = v_inicial

    def aumentaVelocidade(self):
        self.__velocidade = self.__velocidade + 2

    #modifica a velocidade
    def setVelocidade(self, novaVelocidade):
        if novaVelocidade >= 0:
            self.__velocidade = novaVelocidade

carro1 = Carro()
carro1.setVelocidade(10)
print(f'velocidade atual: {carro1.velocidade}')
# print(carro1._Carro__velocidade)
# carro1.__velocidade = 50
# carro1.__velocidade = carro1.__velocidade * -1
# carro1.aumentaVelocidade()
# print(carro1.velocidade)

# carro2 = Carro(10)
# print(f'velocidade do carro2: {carro2.velocidade}')