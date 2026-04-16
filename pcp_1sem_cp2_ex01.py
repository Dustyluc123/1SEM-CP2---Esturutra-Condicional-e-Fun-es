

cod_est = int(input("Digite o código do estado de origem da carga do caminhão (1 até 5): "))

while 1 > cod_est or cod_est > 5:
   cod_est = int(input("Digite um número inteiro compatível (1 até 5): "))

carga_peso = float(input("Digite o peso da carga do caminhão em toneladas: "))

while carga_peso <= 0:
  carga_peso = float(input("Digite o peso da carga do caminhão em toneladas (Um número maior que 0): "))

cod_carga = int(input("Digite o código da carga do caminhão (10 até 40): "))

while cod_carga < 10 or cod_carga > 40:
  cod_carga = int(input("Digite um número inteiro compatível (10 até 40): "))

kg_carga = carga_peso * 1000

print(f'\nO peso da carga do caminhão em quilos é de: {kg_carga}')

if 10 <= cod_carga < 21:
  preço_carga = kg_carga * 100.00
elif 21 <= cod_carga < 31:
  preço_carga = kg_carga * 250.00
elif 31 <= cod_carga < 41:
  preço_carga = kg_carga * 340.00

print(f'\nO preço da carga do caminhão é de: {preço_carga}')

if cod_est == 1:
  imp_carga = preço_carga * 0.35
elif cod_est == 2:
  imp_carga = preço_carga * 0.25
elif cod_est == 3:
  imp_carga = preço_carga * 0.15
elif cod_est == 4:
  imp_carga = preço_carga * 0.05
elif cod_est > 4:
  imp_carga = preço_carga * 0.0

print(f'\nO imposto pago pela carga do caminhão é de: {imp_carga}')

valor_trsp = preço_carga + imp_carga

print(f'\nO valor transportado pelo caminhão é de: {valor_trsp}')