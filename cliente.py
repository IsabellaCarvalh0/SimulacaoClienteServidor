from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
# Envia nome do jogador ao servidor
nomeJogador = input('Digite o nome do jogador:')
clientSocket.send(nomeJogador.encode())
# Envia nível do jogador ao servidor
nivel = input('Digite o nivel do jogador:')
clientSocket.send(nivel.encode())
# Envia jogo desejado ao servidor
jogo = input('Digite o jogo desejado:')
clientSocket.send(jogo.encode())

modifiedSentence = clientSocket.recv(1024)
print ('Resposta do servidor:', modifiedSentence.decode())
clientSocket.close()

