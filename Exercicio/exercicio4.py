vh = int(input('Quanto você ganha por hora?:'))
ht = int(input('Quantas horas você trabalha no mês?'))
salariobruto = (vh) * (ht)

inss = salariobruto % 0.08

ir = salariobruto % 0.11

s = salariobruto % 0.05

descontos = (inss) + (ir) + (s)

sl = salariobruto - descontos


print(salariobruto)
print(ir)
print(inss)
print(s)
print(sl)