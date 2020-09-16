class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=18):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 18

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    fulano = Homem(nome='Fulano')
    beltrano = Homem(fulano, nome='Beltrano')
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
    print(Pessoa.nome_e_atributos_de_classe(), beltrano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(fulano, Pessoa))
    print(isinstance(fulano, Pessoa))
