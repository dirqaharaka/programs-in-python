def reverse_string(input_string):
    result_string = ""
    for char in input_string:
        result_string = char + result_string
    return result_string

user_input = input("Enter a string to reverse: ")
reverse_string = reverse_string(user_input)
print("Reversed string : ", reverse_string)