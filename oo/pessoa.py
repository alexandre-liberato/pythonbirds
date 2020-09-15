class Pessoa:
    def __init__(self, *filhos, nome=None, idade=18):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    fulano = Pessoa(nome='Fulano')
    beltrano = Pessoa(fulano, nome='Beltrano')
    print(Pessoa.cumprimentar(beltrano))
    print(id(beltrano))
    print(beltrano.cumprimentar())
    print(beltrano.nome)
    print(beltrano.idade)
    for filho in beltrano.filhos:
        print(filho.nome)
    beltrano.sobrenome = 'Ciclano'
    del beltrano.filhos
    print(fulano.__dict__)
    print(beltrano.__dict__)