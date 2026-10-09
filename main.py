import random

def par_impar():
    print("_" * 8)
    print(" Bem-vindo ao Jogo Par ou Ímpar")
    print("_" * 40)

    vitorias_usuario = 0
    vitorias_ia = 0

    while True:
        escolha_usuario = input("\nEscolha [P]ar ou [Í]par - S para sair: ").strip().upper()

        if escolha_usuario == 'S':
            print("\nSaindo do jogo..")
            break

        if escolha_usuario not in ['P', 'Í', 'I']:
            print("Escolha inválida. Tente novamente.")
            continue

        if escolha_usuario == 'Í':
            escolha_usuario = 'I'

        try:
            numero_usuario = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue

        numero_ia = random.randint(0, 10)
        soma = numero_usuario + numero_ia

        resultado = "P" if soma % 2 == 0 else "I"

        print(f"\nVocê escolheu: {escolha_usuario}")
        print(f"Você jogou: {numero_usuario}")
        print(f"A IA jogou: {numero_ia}")

        if resultado == escolha_usuario:
            print("Você venceu!")
            vitorias_usuario += 1
        else:
            print("A IA venceu!")
            vitorias_ia += 1

        print(f"\nPlacar: Você {vitorias_usuario} x IA {vitorias_ia}")


if __name__ == "__main__":
    par_impar()