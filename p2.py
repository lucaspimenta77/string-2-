import random


def shuffle_word(word):
    shuffled_word = list(word)
    random.shuffle(shuffled_word)
    return "".join(shuffled_word)


def choose_theme():
    print("Escolha um tema: ")
    print("1 - cidades")
    print("2 - cores")
    print("3 - times")
    print("4 - países")
    print("5 - objetos")
    theme_choice = input("Digite o número correspondente ao tema desejado: ")

    themes = {
        "1": ["paris", "roma", "nova york", "berlim", "pequim", "tóquio"],
        "2": ["vermelho", "azul", "verde", "amarelo", "roxo", "laranja"],
        "3": ["barcelona", "manchester", "milan", "bayern", "real madrid", "juventus"],
        "4": ["brasil", "canadá", "austrália", "japão", "egito", "índia"],
        "5": ["celular", "mesa", "cadeira", "computador", "abajur", "sofá"],
    }

    theme = themes.get(
        theme_choice,
        ["python", "banana", "elefante", "abacaxi", "computador", "laranja"],
    )
    return theme


def choose_difficulty():
    print("Escolha um nivel de dificuldade: ")
    print("1 - Iniciante (7 tentativas)")
    print("2 - Intermediário (5 tentativas)")
    print("3 - Avançado (3 tentativas)")
    difficulty_choice = input("Digite o número correspondente ao nível desejado: ")

    if difficulty_choice == "1":
        return 7
    elif difficulty_choice == "2":
        return 5
    elif difficulty_choice == "3":
        return 3
    else:
        print("Escolha inválida. Nível intermediário foi selecionado por padrão.")
        return 5


def main():
    theme = choose_theme()
    original_word = random.choice(theme)
    shuffled_word = shuffle_word(original_word)
    attempts = choose_difficulty()

    print("Jogo de Adivinhação de Palavras!")
    print("Palavra embaralhada:", shuffled_word)

    while attempts > 0:
        guess = input("Tente adivinhar a palavra: ")
        attempts -= 1
        if guess.lower() == original_word.lower():
            print("Parabens! Voce acertou a palavra.")
            break
        else:
            if attempts > 0:
                print(f"Palavra incorreta. Tente novamente. Tentativas restantes: {attempts}")
            else:
                print("Suas tentativas acabaram. Continue tentando!")

    print(f"A palavra correta era: {original_word}")
    print(f"Número de tentativas utilizadas: {5 - attempts}")


if __name__ == "__main__":
    main()
