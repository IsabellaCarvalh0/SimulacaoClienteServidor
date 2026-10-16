# 🎮 Matchmaking de Jogos com Sockets TCP

Sistema simples de **matchmaking** (formação de partidas) para jogos online, implementado em Python com **sockets TCP** no modelo cliente-servidor. Os jogadores informam seu nome, nível e o jogo desejado; o servidor os coloca em uma fila de espera e, quando há jogadores suficientes, cria uma partida com um ID único.

## 📋 Funcionalidades

- Comunicação cliente-servidor via sockets TCP (`SOCK_STREAM`)
- Filas de espera independentes para cada jogo
- Criação automática de partida quando a fila atinge o número de jogadores necessário
- Geração de ID sequencial para cada partida criada
- Resposta ao cliente informando se ele entrou na fila ou se a partida foi criada
- Tratamento de jogos não suportados

## 🕹️ Jogos suportados

| Jogo | Valor a digitar | Jogadores por partida |
|------|-----------------|-----------------------|
| Valorant | `valorant` | 4 |
| League of Legends | `leagueoflegends` | 5 |
| Counter Strike | `counterstrike` | 4 |
| FIFA | `fifa` | 2 |
| Minecraft | `minecraft` | 3 |

> O nome do jogo não diferencia maiúsculas de minúsculas, mas deve ser digitado **sem espaços** (ex.: `leagueoflegends`).

## 📁 Estrutura do projeto

```
.
├── servidor.py   # Servidor: recebe os jogadores, gerencia as filas e cria as partidas
├── cliente.py    # Cliente: envia nome, nível e jogo desejado e exibe a resposta
└── README.md
```

## ⚙️ Requisitos

- Python 3.x
- Nenhuma biblioteca externa (usa apenas o módulo `socket` da biblioteca padrão)

## 🚀 Como executar

1. **Inicie o servidor** em um terminal:

   ```bash
   python servidor.py
   ```

   Você verá a mensagem: `O servidor esta pronto esperando mensagens`.

2. **Execute o cliente** em outro terminal (repita em vários terminais para simular vários jogadores):

   ```bash
   python cliente.py
   ```

3. Informe os dados solicitados:

   ```
   Digite o nome do jogador: Ana
   Digite o nivel do jogador: 10
   Digite o jogo desejado: fifa
   ```

## 💬 Exemplo de uso

**Primeiro jogador entra na fila:**

```
Resposta do servidor: Você foi adicionado à fila de espera.
Jogo: FIFA
```

**Segundo jogador completa a partida de FIFA:**

```
Resposta do servidor: Partida Criada!
Jogo: FIFA
ID da partida: 1
Participantes: BRUNO ANA
```

**Jogo inexistente:**

```
Resposta do servidor: Jogo não identificado
```

## 🔧 Como funciona

1. O servidor escuta na porta `12000` e aceita uma conexão por vez.
2. O cliente envia, em sequência, o **nome**, o **nível** e o **jogo desejado**.
3. O servidor adiciona o jogador (com o nome em maiúsculas) à fila do jogo escolhido.
4. Se a fila atingir o número de jogadores da partida, o servidor monta a partida, esvazia a fila e incrementa o ID.
5. O servidor responde ao cliente e encerra a conexão.

## ⚠️ Limitações conhecidas

- O servidor atende **um cliente por vez** (sem threads ou conexões simultâneas).
- O **nível** do jogador é recebido e exibido no servidor, mas ainda **não é usado** para formar as partidas.
- Os três valores são enviados em chamadas `send` consecutivas, o que pode fazê-los chegar juntos em um único `recv`. Em redes reais, o ideal é usar um delimitador ou prefixo de tamanho.
- O cliente se conecta a `localhost`; para usar em rede, altere `serverName` em `cliente.py` para o IP do servidor.
- Quem entra primeiro na fila aparece por último na lista de participantes (uso de `pop()`).

## 💡 Ideias de melhoria

- Suporte a múltiplos clientes simultâneos com `threading` ou `asyncio`
- Matchmaking considerando o nível dos jogadores
- Protocolo de mensagens com delimitadores ou JSON
- Menu de seleção de jogos no cliente
- Refatorar as filas em um dicionário para reduzir código repetido

## 📚 Contexto

Projeto desenvolvido para fins educacionais, demonstrando conceitos de programação com sockets e comunicação em redes de computadores.
