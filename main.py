import random

def par_impar():
    print("_" * 8)
    print(" Bem-vindo ao Jogo Par ou Ímpar")
    print("_" * 40)

    vitorias_usuario = 0
    vitorias_ia = 0

    while True:
        escolha_usuario = input("\nEscolha [P]ar ou [Í]par - S para sair").strip()

        if escolha_usuario == 'S':
            print("\nSaindo do jogo..")
            