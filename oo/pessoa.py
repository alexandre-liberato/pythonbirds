class Pessoa:
    olhos = 2

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
    beltrano.olhos = 1
    del beltrano.olhos
    print(fulano.__dict__)
    print(beltrano.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(fulano.olhos)
    print(beltrano.olhos)
    print(id(Pessoa.olhos), id(fulano.olhos), id(beltrano.olhos))