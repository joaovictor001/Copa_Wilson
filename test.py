# Criar um dicionário para os jogadores, uma lista para os pontos e outra lista para o time.
# Onde o USUÁRIO insira um jogador e seu nome será salvo no dicionário.

jogadores = {}
pontos = []
time = []
contador = 0
soma = 0

while True:
    pontos.clear()
    nome = str(input("Digite o nome do jogador: "))
    jogadores["nome"] = nome
    contador += 1
    resp = input("O jogador jogou a partida 'sim ou não' ").upper()[0]
    if resp == "S":
        partidas = int(input("Quantas partidas ele jogou? "))
        for i in range(partidas):
            pontos.append(int(input(f"Qual foi sua pontuação na {i + 1} partida? ")))
        jogadores["pontos"] = pontos[:]
        jogadores["total"] = sum(pontos)
        time.append(jogadores.copy())
    elif resp == "N":
        continue
    else:
        break

    adicionar = input("Deseja adicionar outro jogador?").upper()[0]

    if adicionar == 'S':
        continue
    elif adicionar == 'N':
        print('-=' * 10)
        print(time)
    else:
        print("Valor inválido!")

    id = int(input("Informe o id do jogador que deseja consultar: "))

    if id >= len(time):
        print("Valor inválido! Tente novamente")
    else:
        print("-=" * 16)
        print(f"Nome: {time[id]['nome']} Pontos: {time[id]['pontos']} Total: {time[id]['total']}")
        print("-=" * 16)
    break