def reverse_character_in_words(input_string):
    words = input_string.split()
    reversed_words = []
    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    reversed_sentence =  ' '.join(reversed_words)
    return reversed_sentence

user_input = input("Masukkan sebuah kalimat : ")
reversed_sentense = reverse_character_in_words(user_input)
print("Urutan karakter terbalik : ", reversed_sentense)

