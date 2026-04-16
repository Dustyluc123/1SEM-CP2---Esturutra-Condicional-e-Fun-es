cliente = input('Digite o nome do cliente: ')
idade = int(input('Digite a idade do cliente: '))
renda = float(input('Digite a renda mensal do cliente: '))
valor= float(input('Digite o valor desejado do empréstimo: '))
parcelas = int(input('Digite o número de parcelas a ser pago (3 até 24): '))


def pode_aprovar(Idade, renda, valor):
    if Idade <18:
        return False
    
    elif (renda * 20) < valor :
        return False
    else:
        return True



if pode_aprovar(idade, renda, valor) == True:
    print('Empréstimo aprovado para o cliente', cliente)
    def definir_taxa(parcelas):
        
        if parcelas <= 6:
            taxa =  0.05
        elif parcelas <= 12:
            taxa = 0.08
        else:
            taxa  = 0.1
        return taxa

    taxa = definir_taxa(parcelas)

    def calcular_parcela(valor ,parcelas, taxa):
        pmt = valor * (taxa * (1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1)
        return pmt


    pmt = calcular_parcela(valor, parcelas, taxa)

    def calcular_total(pmt, parcelas):
        total = pmt * parcelas
        return total

    total = calcular_total(pmt, parcelas)

    def calcular_juros(total, valor): 
        juros = total - valor
        return juros

    juros = calcular_juros(total, valor)

    print(f'Nome do cliente: {cliente}')
    print(f'Valor do empréstimo: {valor}')
    print(f'Taxa de juros: {(taxa * 100):.2f}%')
    print(f'Valor da parcela: {pmt:.2f}')
    print(f'Valor total pago: {total:.2f}')
    print(f'Valor dos juros: {juros:.2f}')
    
else:    
    print('Empréstimo não aprovado para o cliente', cliente)
        




