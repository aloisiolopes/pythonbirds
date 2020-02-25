class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome #nome é respectivo a self.nome, quando não tivermos nada será None como declarado a cima

    def cumprimentar(self):
        return f'Óla {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Aloisio')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Renzo'
    print(p.nome)
    print(p.idade)




