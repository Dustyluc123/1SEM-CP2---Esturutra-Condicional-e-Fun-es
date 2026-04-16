

nome = input("Digite o nome do funcionário: ")

cargos = ['1-Gerente',
       '2-Analista',
       '3-Assistente',
       '4-Estagiário']

cargo = input("Digite o cargo do funcionário: ")
while cargo not in cargos:
  cargo = input("Cargo inválido. Digite novamente o número referente ao cargo e anomenclatura do cargo: ")

sálario_b = float(input("Digite o salário do funcionário: "))
while sálario_b <= 0:
  sálario_b = float(input("Salário inválido. Digite novamente o salário do funcionário: "))

hrs_extras = int(input("Digite a quantidade de horas extras trabalhadas: "))

faltas = int(input("Digite a quantidade de faltas do funcionário: "))

b = ['s',
     'n']
bônus = (input("Digite se funcionário recebeu o bônus esse mês (s para sim, n para não): "))
while bônus not in b:
  bônus = (input("Digite se funcionário recebeu o bônus esse mês (s para sim, n para não): "))

if bônus == 's':
   bônus = 1
elif bônus == 'n':
   bônus = 0

if cargo == '1-Gerente':
  bns = 1000
elif cargo == '2-Analista':
  bns = 500
elif cargo == '3-Assistente':
  bns = 300
elif cargo == '4-Estagiário':
  bns = 100

def calc_hrs_extras(horas_extras, sálario_bruto):
  h_ext = (horas_extras * (sálario_bruto * 0.015))
  return h_ext

def calc_faltas(faltas_mensais, sálario_bruto):
  falta = (sálario_bruto * 0.02) * faltas_mensais
  return falta

def calc_bônus(recebeu_bonus, bonus_cargo):
  bonus = recebeu_bonus * bonus_cargo
  return bonus

extras_horas = calc_hrs_extras(hrs_extras, sálario_b)
flts = calc_faltas(faltas, sálario_b)
extras_bônus = calc_bônus(bônus, bns)

def calc_extras(calc_horas_extras, calc_bonus):
  ext = calc_horas_extras + calc_bonus
  return ext

extras = calc_extras(extras_horas, extras_bônus)

def calc_sálario_acrésimo(sálario_bruto, extras_final):
  sálario_acréscimo = sálario_bruto + extras_final
  return sálario_acréscimo

sálario_a = calc_sálario_acrésimo(sálario_b, extras)

def calc_sálario_final(sálario_acréscimo, falta_final):
  sálario_final = sálario_acréscimo - falta_final
  return sálario_final

sálario_f = calc_sálario_final(sálario_a, flts)

print(f'\nOlá {nome}!\nSeu cargo é refere a: {cargo}\nSeu sálario bruto é de: {sálario_b}\nTotal de acrésimos em reais é de: {extras}\nSeu desconto por falta foi de: {flts}\nO sálario final é de: {sálario_f}')