import random

cartas =  [1,2,3,4,5,6,7,8,9,10,11]
naipe =["paus","ouro","espadas","copas"]
cartas_originais=[]
naipes_original = []

carta_escolhida = random.choice(cartas)
naipe_escolhido = random.choice(naipe)

mao_jogador={}

def sortear_carta():
    carta_escolhida = random.choice(cartas)
    return carta_escolhida

def sortear_naipe():
    naipe_escolhido = random.choice(naipe)
    return naipe_escolhido

def sortear_baralho():

    while len(mao_jogador)<3:
        mao_jogador[sortear_carta()] = sortear_naipe()


    for chave, valor in mao_jogador.items():
        cartas_originais.append(chave)
        naipes_original.append(valor)
        
        #print(f"{chave} e {valor}" )

    print(cartas_originais)
    escolha = int(input("escolhe: "))
    print(cartas_originais[escolha - 1])
    print(naipes_original)

    return


jogador1 = sortear_baralho()    
jogador2 = sortear_baralho()

    

     
     




