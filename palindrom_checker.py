def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def palindrom_checker():
    word = input("Enter a word or prase: ")
    if is_palindrome(word):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


palindrom_checker()
