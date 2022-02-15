# import platform
import getpass
# from datetime import datetime


# # print('Nome Máquina:...........', platform.node())
# print('Arquitetura:............', platform.architecture())
# print('Sistema Operacional:....', platform.system())
# print('Versão do SO:...........', platform.release())
# print('Processador:............', platform.processor())
# print('Versão do Python:.......', platform.python_version())

# print('\n',datetime.now())
# print(datetime.now().hour)

usuario = getpass.getuser()
senha = getpass.getpass('Digite sua senha:...')

if usuario == 'su-sa' and senha == 'Hello':
    print('Bem vindo Clodovaldo!')
else:
    print('Você não tem acesso!')


