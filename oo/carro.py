"""
Vôce deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes.
Classes:
1 - Motor
2 - Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1 - atributo de dado velocidade
2 - Método acelerar, que devera incrementar a velocidade em 1.
3 - Método frear, que devera decrementar a velocidade em 2.

A direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:
1 - valor de direção com valores possiveis: norte, sul, leste, oeste.
2 - Metodo girar a direita.
3 - Metodo girar a esquerda.
  N
O   L
  S

Exemplo:
#testando motor

>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0

#testando direção

>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girarDireita()
>>> direcao.valor
'Leste'
>>> direcao.girarDireita()
>>> direcao.valor
'Sul'
>>> direcao.girarDireita()
>>> direcao.valor
'Oeste'
>>> direcao.girarDireita()
>>> direcao.valor
'Norte'
>>> direcao.girarEsquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girarEsquerda()
>>> direcao.valor
'Sul'
>>> direcao.girarEsquerda()
>>> direcao.valor
'Leste'
>>> direcao.girarEsquerda()
>>> direcao.valor
'Norte'

>>> carro = Carro(direcao, motor)
>>> carro.calculoVelocidade()
0
>>> carro.acelerar()
>>> carro.calculoVelocidade()
1
>>> carro.acelerar()
>>> carro.calculoVelocidade()
2
>>> carro.frear()
>>> carro.calculoVelocidade()
0
>>> carro.calculoDirecao()
'Norte'
>>> carro.girarDireita()
>>> carro.calculoDirecao()
'Leste'
>>> carro.girarErquerda()
>>> carro.calculoDirecao()
'Norte'
>>> carro.girarErquerda()
>>> carro.calculoDirecao()
'Oeste'

"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

class Direcao:
    virarDireita = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    virarEsquerda = {OESTE: SUL, SUL: LESTE, LESTE:NORTE, NORTE: OESTE}
    def __init__(self):
        self.valor = NORTE


    def girarDireita(self):
        self.valor = self.virarDireita[self.valor]

    def girarEsquerda(self):
        self.valor = self.virarEsquerda[self.valor]


motor = Motor()
direcao = Direcao()