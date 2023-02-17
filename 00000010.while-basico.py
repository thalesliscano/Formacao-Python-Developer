# opcao = -1
# Pedir um numero pro usuário, se for par vai exibir o número, continua executando, se for ímpar vai exibir, se o número for 10
# while opcao != 0:
while True:
  opcao = int(input("informe um número: "))
  if opcao / 2 == 0 or opcao / 2 == 1:
    continue
  elif opcao  == 10:
    break
print(opcao)

