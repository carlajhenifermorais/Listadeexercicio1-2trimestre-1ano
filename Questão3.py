# Faça um programa em Python que receba três números reais, calcule e mostre a multiplicação desses números. O resultado da multiplicação deve ter apenas uma casa decimal.

x = float(input("Informe o primeiro número: "))
y = float(input("Informe o segundo número: "))
z = float(input("Informe o terceiro número: "))
r = x * y * z
print(f"O resultado é {r:.1f}")