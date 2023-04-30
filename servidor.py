import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 50000  # Porta para ouvir conexões

# Socket servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4, TCP
servidor.bind((HOST, PORT)) # Vincula end e port ao socket para escuta
servidor.listen() # Escutar conexões simultaneas 

print(F'\nServidor escutando em:\nIP-> {HOST}\nPORTA-> {PORT}\n')

while True:
    # Aguadando conexão
    cliente, endereco = servidor.accept() # Aceitando novas conexoes como servidor
    print(f'Conexão recebida de {endereco}')

    numero = cliente.recv(1024).decode() # recebe número enviado pelo cliente
    print(f'Número recebido: {numero}\n')

    # Verificando tamanho do numero
    if len(numero) > 10:
        resposta = str(numero).encode()
    else:
        if int(numero) % 2 == 0:
            resposta = 'PAR'.encode()
        else:
            resposta = 'ÍMPAR'.encode()

    cliente.send(resposta)  # Enviando resposta para cliente
    cliente.close()  # Encerra conexão com o cliente