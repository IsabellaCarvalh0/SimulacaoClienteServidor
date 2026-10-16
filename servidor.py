from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

valorant = []
leagueOfLegends = []
counterStrike = []
fifa = []
minecraft = []

idDaPartida = 1
print('O servidor esta pronto esperando mensagens')
while True:
	connectionSocket, addr = serverSocket.accept()
	nomeJogador = connectionSocket.recv(1024).decode()
	print("Nome do Jogador: ", nomeJogador)
	capitalizedNomeJogador = nomeJogador.upper()

	nivel = connectionSocket.recv(1024).decode()
	print("Nível do jogador: ", nivel)

	jogo = connectionSocket.recv(1024).decode()
	print("Jogo: ", jogo)
	capitalizedJogo = jogo.upper()

	if capitalizedJogo == "VALORANT":
		valorant.append(capitalizedNomeJogador)
		if len(valorant) == 4:
			mensagem = "Partida Criada! \nJogo: Valorant \nID da partida: "+str(idDaPartida) +"\nParticipantes: "
			for i in range(4):
				mensagem = mensagem + valorant.pop()+" "
			idDaPartida = idDaPartida + 1
		else:
			mensagem = "Você foi adicionado à fila de espera.\nJogo: Valorant"
	elif capitalizedJogo == "LEAGUEOFLEGENDS":
		leagueOfLegends.append(capitalizedNomeJogador)
		if len(leagueOfLegends) == 5:
			mensagem = "Partida Criada! \nJogo: League of Legends \nID da partida: "+str(idDaPartida) +"\nParticipantes: "
			for i in range(5):
				mensagem = mensagem + leagueOfLegends.pop()+" "
			idDaPartida = idDaPartida + 1
		else:
			mensagem = "Você foi adicionado à fila de espera.\nJogo: League of Legends"
	elif capitalizedJogo == "COUNTERSTRIKE":
		counterStrike.append(capitalizedNomeJogador)
		if len(counterStrike) == 4:
			mensagem = "Partida Criada! \nJogo: Counter Strike \nID da partida: "+str(idDaPartida) +"\nParticipantes: "
			for i in range(4):
				mensagem = mensagem + counterStrike.pop()+" "
			idDaPartida = idDaPartida + 1
		else:
			mensagem = "Você foi adicionado à fila de espera.\nJogo: Counter Strike"
	elif capitalizedJogo == "FIFA":
		fifa.append(capitalizedNomeJogador)
		if len(fifa) == 2:
			mensagem = "Partida Criada! \nJogo: FIFA \nID da partida: "+str(idDaPartida) +"\nParticipantes: "
			for i in range(2):
				mensagem = mensagem + fifa.pop()+" "
			idDaPartida = idDaPartida + 1
		else:
			mensagem = "Você foi adicionado à fila de espera.\nJogo: FIFA"
	elif capitalizedJogo == "MINECRAFT":
		minecraft.append(capitalizedNomeJogador)
		if len(minecraft) == 3:
			mensagem = "Partida Criada! \nJogo: Minecraft \nID da partida: "+str(idDaPartida) +"\nParticipantes: "
			for i in range(3):
				mensagem = mensagem + minecraft.pop()+" "
			idDaPartida = idDaPartida + 1
		else:
			mensagem = "Você foi adicionado à fila de espera.\nJogo: Minecraft"
	else:
		mensagem = "Jogo não identificado"
	print("mensagem que sera enviada: ", mensagem)
	connectionSocket.send(mensagem.encode())
	connectionSocket.close()
