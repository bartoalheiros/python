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
        if novaVelocidade >= 0 and novaVelocidade < 50:
            self.__velocidade = novaVelocidade

    def getVelocidade(self):
        return self.__velocidade

carro1 = Carro()
print(f'velocidade atual: {carro1.getVelocidade()}')
carro1.setVelocidade(10)
print(f'velocidade atual: {carro1.getVelocidade()}')
# print(carro1._Carro__velocidade)
# carro1.__velocidade = 50
# carro1.__velocidade = carro1.__velocidade * -1
# carro1.aumentaVelocidade()
# print(carro1.velocidade)

# carro2 = Carro(10)
# print(f'velocidade do carro2: {carro2.velocidade}')