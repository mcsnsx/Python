import platform # ---------------------------> import info. maquina
import getpass # ----------------------------> import usuário da maquina
from datetime import datetime # -------------> import data

# --> Especificações da maquina
print("Nome da maquina:.......................", platform.node())
print("Arquitetura:...........................", platform.architecture())
print("Sistema Operacional:...................", platform.system())
print("Versão do SO:..........................", platform.release())
print("Processador:...........................", platform.processor())
print("Versão do Python:......................", platform.python_version())

# --> Especificação da data e hora
print(datetime.now()) # ----------> data e hora completa
print(datetime.now().year) # ----------> apenas o ano
print(datetime.now().hour) # ----------> apenas a hora
print(datetime.now().day) # -----------> apenas o dia
print(datetime.now().month) # ---------> apenas o mes

# --> Busca o usuário da maquina / login e senha
usuario = getpass.getuser() # -------------------------> usuário da maquina
senha = getpass.getpass("Digite sua senha:.....") # ---> senha

# --> Condição para validar usuário e senha
if usuario == 'Maria' and senha == 'Hello':
    print('Bem vinda!')
else:
    print('Você não tem acesso!')
