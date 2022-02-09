# USO DO A (append) ---> ACRESCENTA AO ARQUIVO EXISTENTE
#with open("primeiro_arquivo.txt", "a") as arquivo:
#   arquivo.write("\nHakuna Matata")

# USO DO W (write) ---> CRIA UM NOVO ARQUIVO
#with open("primeiro_arquivo.txt", "w") as arquivo:
#   arquivo.write("\nHakuna Matata")

# USO DO R (read) ---> LÊ O ARQUIVO
#with open("primeiro_arquivo.txt", "r") as arquivo:
#   conteudo = arquivo.read()
#   print(conteudo)

#   arquivo.readline() ----> SÓ LÊ A PRIMEIRA LINHA

# LÊ CADA UMA DAS LINHAS
#with open("primeiro_arquivo.txt", "r") as arquivo:
#    for linha in arquivo.readlines():
#        print(linha)

with open("primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
