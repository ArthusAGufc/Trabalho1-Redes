# Trabalho 1 - Redes

Programa servidor:
1. Para o funcionamento é necessário realizar a importação da biblioteca "socket"
2. Em seguida é necessário definir um endereço IP para o seu servidor e uma porta para que os clientes possam acessá-lo
3. Nas linhas 7, 8 e 9 é feita a criação do servidor.
4. Dentro do laço é onde ocorre a interação entre o cliente e o servidor, onde na linha 15 a conexão é realizada e na linha 30 é retornada uma resposta para o programa cliente.
5. Por fim, na linha 31 é encerrada a conexão

Programa cliente:
1. Assim como no programa servidor, é necessário importar a biblioteca "socket"
2. O endereço IP e a porta devem ser os mesmos do servidor para que a conexão seja feita com sucesso
3. Dentro do laço ocorre a interação e as configurações da linha 11 devem ser as mesmas passadas durante a configuração do servidor na linha 7 do programa servidor
4. Na linha 12 é solicitada a conexão com o servidor que possua o endereço e a porta especificadas.
5. Na linha 25 a conexão é encerrada e na linha 26 o método sleep é responsável por fazer o processo dentro do loop ser repetido após 10 segundos de espera. 
