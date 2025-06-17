menu = """
==================================
   Bem vindo ao Banco MoneyMoney
[1]Depósito
[2]Saque
[3]Extrato
[4]Sair
==================================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao =="1":
        valor = float(input("Informe o valor do depósito:"))
        if valor > 0:
            saldo += valor
            print ("Depósito realizado com sucesso")
        else:
            print ("Valor inválido! Favor informar outro valor")    
    elif opcao =="2":
        valor = float(input("Informe o valor do saque:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print ("Saldo indisponível")
        elif excedeu_limite:
            print ("Valor acima do limite por saque! Informe outro valor")
        elif excedeu_saques:
            print ("Limite de saques diárias atingido!")        
        elif valor >0:
            saldo -= valor
            extrato += f"Saque R${saldo:.2f}\n"
            numero_saques += 1
        else:
            print ("Saldo insulficiente! Operação não pode ser concluido")    
    elif opcao == "3":
        print ("Extrato")
        print ("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\nSaldo: R${saldo:.2f}")
    elif opcao =="4":
        break
    else:
        print ("Opção inválida! Digite novamente a opão desejada")