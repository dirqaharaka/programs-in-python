def reverse_words_order(input_string):
    words = input_string.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

user_input = input("Masukkan sebuah kalimat : ")
reversed_order = reverse_words_order(user_input)
print("Urutan Kata dibalik : ", reversed_order)