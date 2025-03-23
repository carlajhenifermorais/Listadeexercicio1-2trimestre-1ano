# Dados de Entrada: Quantidade de cavalos. O dono de um haras precisa fazer compras de ferraduras para equipar todos os seus cavalos. Escreva um programa em Python que calcule quantas ferraduras ele deve comprar considerando que ele deve comprar 15% a mais de ferraduras para reserva.

quantcavalos = int(input("Informe a quantidade de cavalos:"))
ferraduras = quantcavalos * 4
ferradurasreserva = ferraduras * 0.15
quantferraduras = ferraduras + ferradurasreserva
print(f"Você deve comprar {quantferraduras:.0f} ferraduras")