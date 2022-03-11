from socket import *

host = input('Insira o ip: ')

porta_inicial = int(input('\nInsira o primeira porta do intervalo: '))

porta_final = int(input('\nInsira a última porta do intervalo: '))


for porta in range(porta_inicial, porta_final+1):

    sock = socket(AF_INET, SOCK_STREAM)

    resultado = sock.connect_ex((host, 21))
    if resultado == 0:
        try:
            servico = getservbyport(porta)
            print(porta, "-", servico)
        except:
            pass

    sock.close()
