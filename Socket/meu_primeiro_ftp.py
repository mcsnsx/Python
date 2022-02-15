from ftplib import *

# ---> Protocolo FTP - Transferencia de arquivos
ftp = FTP ('ftp.ibiblio.org')

print(ftp.getwelcome())

ftp.quit()