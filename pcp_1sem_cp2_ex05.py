cliente = input('Digite o nome do cliente: ')
idade = int(input('Digite a idade do cliente: '))
renda = float(input('Digite a renda mensal do cliente: '))
valor= float(input('Digite o valor desejado do empréstimo: '))
parcelas = int(input('Digite o número de parcelas a ser pago (3 até 24): '))

def pode_aprovar(Idade, renda, valor):
    if Idade >= 18:
        return 'aprovado.'
    
    if (renda * 20) >= valor :
        return 'aprovado.'

def definir_taxa(numero_parcelas):
    
    if numero_parcelas <= 6:
        taxa =  0.05
    elif numero_parcelas <= 12:
        taxa = 0.08
    else:
        taxa  = 0.1
    return taxa

taxa = definir_taxa(numero_parcelas)

def calcular_parcela(emprestimo, numero_parcelas, taxa):
    valor_parcela = (emprestimo *  (taxa)) / numero_parcelas
    return valor_parcela

valor_parcela = calcular_parcela(emprestimo, numero_parcelas, taxa)

def calcular_total(valor_parcela, numero_parcelas):
    valor_total = valor_parcela * numero_parcelas
    return valor_total

valor_total = calcular_total(valor_parcela, numero_parcelas)


    




