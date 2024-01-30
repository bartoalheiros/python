# from pessoa import Pessoa
from produto import Produto

# p1 = Pessoa.por_ano_nascimento('Luiz', 1992)
# p1 = Pessoa('Luiz', 32)
# print(p1)
# print(p1.nome, p1.idade)
# p1.get_ano_nascimento()
# print(Pessoa.gera_id())
# print(p1.gera_id())

p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.preco)