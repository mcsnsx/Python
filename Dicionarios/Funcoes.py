def perguntar():
    return input("O que deseja realizar?\n" +
              "<I> - Para inserir um usuário\n" +
              "<P> - Para pesquisar um usuario\n" +
              "<E> - Para excluir um usuario\n" +
              "<L> - Para listar um usuário: ").upper()

def inserir (dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a ultma data de acesso: "),
                                                   input("Qual a ultima estação acessada: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

#def remover(dicionario):
#    with open("bd.txt", "e") as arquivo:
#       print("Qual usuário gostaria de remover?")
#       usuario = inserir(dicionario)
#       usuario.remove(usuario)