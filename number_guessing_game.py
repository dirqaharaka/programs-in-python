import random

def number_guessing_game():
    target_number = random.randint(1,100)
    while True:
        guess = int(input("masukkan angka tebakan anda 1 - 100 :"))
        if guess == target_number:
            print("Congratulation! Tebakan Anda Benar")
            break
        elif guess < target_number:
            print("Tebakan Anda lebih kecil")
            break
        else:
            print("tebakan anda lebih besar")


number_guessing_game()