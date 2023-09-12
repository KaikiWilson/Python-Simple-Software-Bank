from datetime import date

today = date.today()
data = today.strftime("%d/%m/%Y")

menu = f"""
===========================================
🤔 bem vindo! O que deseja fazer hoje? 🤔

[d] Depositar 💰
[s] Sacar 🤑
[e] Extrato 📃
[q] Sair 🚪

⏰ Data de hoje: {data} ⏰
===========================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_de_deposito = float(input(f"Qual o valor à ser depositado? \n"))
        
        if valor_de_deposito > 0:
            saldo += valor_de_deposito
            extrato += f"O valor de R${valor_de_deposito: .2f} foi depositado na sua conta no dia {data}.\n"
        else:
            print("Valor inválido, insira um valor disponivel da sua conta.")



    elif opcao == "s":
        valor_de_saque = float(input(f"Qual o valor à ser sacado da sua conta?\n"))

        if numero_saques < LIMITE_SAQUES and valor_de_saque <= limite and saldo > 0:
            saldo -= valor_de_saque
            numero_saques += 1
            extrato += f"O valor de {valor_de_saque: .2f} foi sacado da sua conta no dia {data}.\n"

        elif valor_de_deposito > limite:
            print(f"O limite de saque é R$ {limite}.\nPor favor, saque um valor dentro do limite.")
        
        elif saldo <= 0:
            print(f"Não será possível efetuar o depósito por insuficiência de saldo em conta.")

        elif valor_de_saque <= 0:
            print(f"Valor inválido, insira um valor válido.")

        elif numero_saques > LIMITE_SAQUES:
            print(f"Você excedeu o limite de saques diários.\nPor favor, aguarde a recuperação do seu limite diário.")
            break

    elif opcao == "e":
        "=========================================================================="
        print("Sua conta não tem movimentações!" if not extrato else extrato)
        print(f"\nSALDO ATUAL: {saldo: .2f}")
        print(f"\n\nDATA DE VISUALIZAÇÃO DO EXTRATO: {data}")
        "========================================================================="

    elif opcao == "q":
        print(f"""
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                    
Kaiki.DEV say: Obrigado por testar o software! Até depois 😉
                    
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
              """)
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")