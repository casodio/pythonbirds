class Pessoa:
    def __init__(self, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Olá mundo!'

if __name__ == '__main__':
    p = Pessoa('Max')
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)