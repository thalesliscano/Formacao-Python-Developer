# Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

# Entrada
# A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

# Saída
# Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

# Exemplo de Entrada	Exemplo de Saída
# 4
# 56234523485723854755454545478690 78690
# 5434554 543
# 1243 1243
# 54 64545454545454545454545454545454554

# encaixa
# nao encaixa
# encaixa
# nao encaixa
import sys
# N = int(input())
# contador = N

# resposta = []
# while(contador > 0):
#   A,B = map(int,input().split())
#   if (A > 0 and B > 0) and (len(str(A)) <= 1000 and len(str(B)) <= 1000): # Verifica se é maior que 0
#     # Verifica sem possuí um número de digítos menor que 1000
#     valor_digito_B = len(str(B)) # Pega o valor de digíto de B
#     A = str(A)
#     ultimos_digitos_A = A[-valor_digito_B:]
#     if ultimos_digitos_A == str(B):
#       resposta.append("encaixa")
#     else:
#         resposta.append("nao encaixa")
#     contador -= 1
#   else:
#     resposta.append("nao encaixa")
#     contador -= 1
 
# for items in resposta:
#   print(items)


import sys

N = int(sys.stdin.readline())

for i in range(N):
   a,b = sys.stdin.readline().strip().split()
 
   if a.endswith(b):
     sys.stdout.write("encaixa\n")
   else:
    sys.stdout.write("nao encaixa\n")
   









# N = int(sys.stdin.readline())
# n = N
# while n > 0:
#   A, B = sys.stdin.readline(1000).strip().split()

#   if A.endswith(B):
#     sys.stdout.write("encaixa\n")
#   else:
#     sys.stdout.write("nao encaixa\n")
#   n -= 1