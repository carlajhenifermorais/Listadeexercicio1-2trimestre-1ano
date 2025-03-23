#  Um funcionário recebe um salário fixo mais 6.5% de comissão sobre as vendas. Faça um programa em Python que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre o que ele ganhou de comissão e depois o seu salário final, que deve aparecer padronizado com duas casas decimais.

salariofixo = float(input("Informe seu salário fixo: "))
valorvendas = float(input("Informe o valor das suas vendas: "))
comissao = valorvendas * 0.065
salariofinal = round(salariofixo + comissao)
print(f"Você ganhou R${comissao:.2f} e seu salário final foi de R${salariofinal:.2f}")
