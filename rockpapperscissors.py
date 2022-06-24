import random
print("Bem vindo ao pedra, papel e tesoura!")

numero_rodadas = input("Quantas rodadas desejas jogar?:")
numero_rodadas = int(numero_rodadas)

list = (['pedra', 'papel', 'tesoura'])

jogador = 0
robo = 0


for i in range(numero_rodadas):
    player = input("Faça sua jogada:")
    player = str(player)
    a = random.choice(list)

    if a == "pedra" and player == "papel":
        jogador += 1
        print(f"O computador escolheu {a}")
        print("Você venceu!")
        print(f"{jogador} vs {robo}")
    
    elif a == "pedra" and player == "tesoura":
        robo += 1
        print(f"O computador escolheu {a}")
        print("Você perdeu!")
        print(f"{jogador} vs {robo}")

    elif a == "pedra" and player == "pedra":
        print(f"O computador escolheu {a}")
        print("Foi empate!")
        print(f"{jogador} vs {robo}")

    #----------------------------------------------------

    if a == "papel" and player == "tesoura":
        jogador += 1
        print(f"O computador escolheu {a}")
        print("Você venceu!")
        print(f"{jogador} vs {robo}")

    elif a == "papel" and player == "pedra":
        robo += 1
        print(f"O computador escolheu {a}")
        print("Você perdeu!")
        print(f"{jogador} vs {robo}")
    
    elif a == "papel" and player == "papel":
        print(f"O computador escolheu {a}")
        print("Foi empate!")
        print(f"{jogador} vs {robo}")

    
    #---------------------------------------------------

    if a == "tesoura" and player == "pedra":
        jogador += 1
        print(f"O computador escolheu {a}")
        print("Você venceu!")
        print(f"{jogador} vs {robo}")

    elif a == "tesoura" and player == "papel":
        robo += 1
        print(f"O computador escolheu {a}")
        print("Você perdeu!")
        print(f"{jogador} vs {robo}")

    elif a == "tesoura" and player == "tesoura":
        print(f"O computador escolheu {a}")
        print("Foi empate!")
        print(f"{jogador} vs {robo}")

    
    
    


print(f"O jogo terminou em {jogador} x {robo}")
if jogador > robo:
    print("Jogador venceu!")
elif jogador < robo:
    print("Computador venceu!")
else:
    print("Foi empate!")
