arquivo = int(input('Quantos MB tem seu arquivo?'))
velocidade = int(input('Qual a velocidade do link na Internet em MBS?'))
calculo = (arquivo) / (velocidade)
tempo = (calculo) / 60
print(tempo)