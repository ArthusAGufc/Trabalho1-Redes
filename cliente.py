import socket
import time
import random

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 50000  # Porta para se conectar ao servidor

while True: # laço infinito

    # Socket cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4, TCP
    cliente.connect((HOST, PORT))  # Conectando ao servidor

    expoente = random.randint(1, 30) # sorteando casas decimais de 1 a 30
    numero = str(random.randint(1, 10**expoente)) # gera um numero de 1 a ate no maximo 10 elevado a 30

    cliente.send(numero.encode()) # Enviando o número para servidor
    resposta = cliente.recv(1024).decode() # Resposta do servidor
    
    if len(resposta) < 10:
        print(f'Resposta do servidor: {resposta}') # Imprime a resposta 
    else:
        print(f'Resposta do servidor: {resposta} FIM') # Imprime a resposta 

    cliente.close() # Encerra conexão com servidor
    time.sleep(1) # Aguardo 10 segundos 
