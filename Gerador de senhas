import random

print("Bem-vindo ao meu gerador de senhas!")

chars = "abcdefghijklmnopqrstuvwxyz!@#-_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

quantidade = input("Quantas senhas deseja gerar?:")
quantidade = int(quantidade)

print(f"Gerando {quantidade} quantidades...")

tamanho = input("Qual vai ser o tamanho da senha?:")
tamanho = int(tamanho)

def senha(quantidade, tamanho):
    for i in range(quantidade):
        senhas = ''
        for c in range(tamanho):
            senhas += random.choice(chars)
        print(senhas)

senha(quantidade, tamanho)
