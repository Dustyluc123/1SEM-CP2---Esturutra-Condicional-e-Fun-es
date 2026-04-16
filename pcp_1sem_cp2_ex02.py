#Questão 2

lado_a = float(input("Digite o valor do lado A do triângulo: "))
lado_b = float(input("Digite o valor do lado B do triângulo: "))
lado_c = float(input("Digite o valor do lado C do triângulo: "))

while lado_b > lado_a or lado_c > lado_a:
   print(f'Digite os valores de modo que o maior seja o lado A')
   lado_a = float(input("Digite o valor do lado A do triângulo: "))
   lado_b = float(input("Digite o valor do lado B do triângulo: "))
   lado_c = float(input("Digite o valor do lado C do triângulo: "))

print(f'\nOs valores dos lados do triângulo são: Lado A ={lado_a}, Lado b = {lado_b} e Lado C ={lado_c}, sendo A o lado maior')

if lado_a >= lado_b + lado_c:
  print(f'NÃO FORMA TRIÂNGULO')
elif lado_a == lado_b == lado_c:
  print(f'TRIÂNGULO EQUILÁTERO')
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
  print(f'TRIÂNGULO ISÓSCELES')
elif lado_a**2 == lado_b**2 + lado_c**2:
  print(f'TRIÂNGULO RETÂNGULO')
elif lado_a**2 > lado_b**2 + lado_c**2:
  print(f'TRIÂNGULO OBTUSÂNGULO')
elif lado_a**2 < lado_b**2 + lado_c**2:
  print(f'TRIÂNGULO ACUTÂNGULO')