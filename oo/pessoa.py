class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome #nome é respectivo a self.nome, quando não tivermos nada será None como declarado a cima
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Óla {id(self)}'


if __name__ == '__main__':
    Luiza = Pessoa(nome='Luiza')
    Aloisio = Pessoa(Luiza, nome='Aloisio')
    print(Pessoa.cumprimentar(Aloisio))
    print(id(Aloisio))
    print(Aloisio.cumprimentar())
    print(Aloisio.nome)
    print(Aloisio.idade)
    for filhos in Aloisio.filhos:
        print(filhos.nome)





