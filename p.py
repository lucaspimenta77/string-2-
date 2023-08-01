import random

def shuffle_word(word):
    shuffled_word = list(word)
    random.shuffle(shuffled_word)
    return ''.join(shuffled_word)

def main():
    word_list = ["python", "banana", "elefante", "abacaxi", "computador", "laranja"]
    original_word = random.choice(word_list)
    shuffled_word = shuffle_word(original_word)
    attempts = 5

    print("Jogo de Adivinhação de Palavras!")
    print("Palavra embaralhada:", shuffled_word)

    while attempts > 0:
        guess = input("Tente adivinhar a palavra: ")
        attempts -= 1

        if guess.lower() == original_word.lower():
            print("Parabéns! Você acertou a palavra.")
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
