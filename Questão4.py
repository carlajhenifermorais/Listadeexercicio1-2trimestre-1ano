# Faça um programa em Python que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 1.5 para a primeira e peso 3.2 para a segunda. 

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
p1 = nota1 * 1.5
p2 = nota2 * 3.2
sn= p1 + p2
sp = 1.5 + 3.2
total = sn / sp
print(f"A média ponderada é {total}")