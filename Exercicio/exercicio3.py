valorinicialinvestido = int(input('Qual o valor inicial investido?'))
rentabilidadeinicial = int(input('Qual a sua rentabilidade?'))
meses = int(input('Quantos meses vc deseja deixar seu dinheiro rendendo?'))

rentabilidade = rentabilidadeinicial % 0.1

valorfinal = valorinicialinvestido *(1 + rentabilidade) ** meses
print(valorfinal)