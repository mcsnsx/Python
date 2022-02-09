from Lista_Funcoes.IdentificacaoDeFuncoes import *

minhaLista=[]
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibindo")
exibirInvertario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)
print("Alterando")
depreciarPorNome(minhaLista, 20)

print("Excluindo")
print(excluirPorSerial(minhaLista))
exibirInvertario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)