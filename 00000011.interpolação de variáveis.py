nome = "Thales"
idade = 20
profissão = "Programador"
linguagem = "Pyhon"


saldo = 4.3434
# Biblioteca
dados = {"nome":"Thales","idade": 20}

# Formas de formatar %s = string | %d = int | %f = float|
print("Nome: %s Idade: %d" % (nome,idade))
print("Nome: {} Idade: {}".format(nome,idade))
print("Nome: {1} Idade: {0}".format(idade,nome))# mostrando índices
print("Nome: {1} Idade: {0} Nome: {1}".format(idade,nome))# reaproveitamento de variável
print("Nome: {nome} Idade: {idade}".format(nome=nome,idade=idade))# identificador dentro das chaves
print("Nome: {nome} Idade: {idade}".format(**dados))# Com biblioteca
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} saldo: {saldo:10.2f}") # Formatação com espaços e de casas decimais








