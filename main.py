#Projeto 1 - Desenvolvimento de Game em linguagem Python - Versão 1

#Import
import random
from os import system, name

#Função para limpar a tela a cada execução
def limpa_tela():

    #Windows
    if name == 'nt':
        _ = system('cls')

    # Mac or Linux
    else:
        _ = system('clear')

#Função
def game():

    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")

    #Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    #list comprehension
    letras_descobertas = ['_' for letras in palavra]

    #Numero de chances
    chances = 6

    #Lista para as letras erradas
    letras_erradas = []

    #Loop enquanto o numero de chances for maior que zero
    while chances > 0:

        #Print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:"," ".join(letras_erradas))

        #Tentativas
        tentativa = input("\nDigite uma letra: ").lower()

        #Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        #Condicional
        if '_' not in letras_descobertas:
            print("\n Voce venceu, a palavra era:", palavra)
            break

    # Condicional
    if '_'  in letras_descobertas:
        print("\n Voce perdeu, a palavra era:", palavra)



#Bloco Main
if __name__ == "__main__":
    game()
    print("\nParabens!!!")