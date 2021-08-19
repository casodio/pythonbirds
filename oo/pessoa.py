class Pessoa:
    olhos = 2
    def __init__(self,*filhos,  nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá mundo!'

if __name__ == '__main__':
    marcio = Pessoa(nome='Marcio')
    max = Pessoa(marcio, nome='Max')

    print(max.cumprimentar())
    print(max.nome)
    print(max.idade)
    for filho in max.filhos:
        print(filho.nome)

    max.sobrenome = 'Maia'
    print(max.sobrenome)
    del max.filhos
    marcio.olhos = 1
    del marcio.olhos

    print(max.__dict__)
    print(marcio.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(max.olhos)
    print(marcio.olhos)

