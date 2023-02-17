# Desafio banco
menu = """
[s] Saque
[d] Depósito
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITES_SAQUES = 3

while True:
  opcao = input(menu)
  
  if opcao == "d":
    valor = float(input("Quanto deseja depositar: "))

    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n" 
    else:
      print("Operação falhou! O valor informado é inválido.")

  elif opcao == "s":
    valor = float(input("Quanto deseja sacar: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITES_SAQUES

    if excedeu_saldo:
      print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
      print("Operação falhou! Limite excedido.")
    elif excedeu_saques:
      print("Operação falhou! Numeros de saques por dia excedidos.")

    elif valor > 0:
      saldo -= valor 
      extrato += f"Saque: R$ {valor:.2f}\n"
      numero_saques += 1 
    else:
      print("Operação falhou! O valor informado é inválido." )

  elif opcao == "e":
      print("EXTRATO".center(21,"="))
      print("Não foram realizadas movimentaçãoes." if not extrato else extrato)
      print(f"R$ {saldo:.2f}")
      print(20 * "=")

  elif opcao == "q":
    break
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")

