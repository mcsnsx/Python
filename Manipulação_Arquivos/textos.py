# MANIPULAÇÃO DE STRINGS


texto = "Leia e Han Solo"
        #012345678901234
        #543210987654321 ---> voltando os caracteres
print((texto[0:4])) #-------> posição dos caracteres
print((texto[0:4:2])) #-----> printar os caracteres de 2 em 2
print(texto[7:]) #----------> printar da posição 7 em diante
print(texto[-8:]) #---------> contagem voltando os caracteres
print(texto[::-1]) #--------> printa os caracteres de trás pra frente

# 0:4:2
# posição inicial : quantidade de informação percorrida : passo(quando vai andar)