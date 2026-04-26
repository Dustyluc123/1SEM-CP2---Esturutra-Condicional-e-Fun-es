nome = input("Digite o nome do funcionário: ")

cargos = ['1-Gerente',
       '2-Analista',
       '3-Assistente',
       '4-Estagiário']

cargo = input("Digite o cargo do funcionário: ")

while cargo not in cargos:
  cargo = input("Cargo inválido. Digite novamente o número referente ao cargo e anomenclatura do cargo: ")

salario_b = float(input("Digite o salário do funcionário: "))

while salario_b <= 0:
  salario_b = float(input("Salário inválido. Digite novamente o salário do funcionário: "))

hrs_extras = int(input("Digite a quantidade de horas extras trabalhadas: "))

faltas = int(input("Digite a quantidade de faltas do funcionário: "))

b = ['s',
     'n']
bonus = (input("Digite se funcionário recebeu o bonus esse mês (s para sim, n para não): "))

while bonus not in b:
  bonus = (input("Digite se funcionário recebeu o bonus esse mês (s para sim, n para não): "))

if bonus == 's':
   bonus = 1
elif bonus == 'n':
   bonus = 0

if cargo == '1-Gerente':
  bns = 1000
elif cargo == '2-Analista':
  bns = 500
elif cargo == '3-Assistente':
  bns = 300
elif cargo == '4-Estagiário':
  bns = 100

def calc_hrs_extras(horas_extras, salario_bruto):
  h_ext = (horas_extras * (salario_bruto * 0.015))
  return h_ext

def calc_faltas(faltas_mensais, salario_bruto):
  falta = (salario_bruto * 0.02) * faltas_mensais
  return falta

def calc_bonus(recebeu_bonus, bonus_cargo):
  bonus = recebeu_bonus * bonus_cargo
  return bonus

extras_horas = calc_hrs_extras(hrs_extras, salario_b)
flts = calc_faltas(faltas, salario_b)
extras_bonus = calc_bonus(bonus, bns)

def calc_extras(calc_horas_extras, calc_bonus):
  ext = calc_horas_extras + calc_bonus
  return ext

extras = calc_extras(extras_horas, extras_bonus)

def calc_salario_acrescimo(salario_bruto, extras_final):
  salario_acrescimo = salario_bruto + extras_final
  return salario_acrescimo

salario_a = calc_salario_acrescimo(salario_b, extras)

def calc_salario_final(salario_acrescimo, falta_final):
  salario_final = salario_acrescimo - falta_final
  return salario_final

salario_f = calc_salario_final(salario_a, flts)

print(f'\nOlá {nome}!\nSeu cargo é: {cargo}\nSeu salário bruto é de: {salario_b}\nTotal de acréscimos, em R$, é de: {extras}\nSeu desconto por falta foi de: {flts}\nO salario final é de: {salario_f}')