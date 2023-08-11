import os
import datetime

def write_entry(entry):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = f"diary_{date}.txt"
    with open(filename, 'a') as file:
        file.write(entry + '\n')
    print("Enry saved successfully")

def read_entries():
    print("Your Diary Entries: ")
    for file in os.listdir():
        if file.startswith("diary_") and file.endswith(".txt"):
            with open(file, 'r') as f:
                content = f.read()
                print(content)

def personal_diary_app():
    print("Welcome to your Personal Diary!")
    while True:
        print("\nOptions:")
        print("1. Write Entry")
        print("2. Read Entries")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            entry = input("Write your diary entry:")
            write_entry(entry)
        elif choice == '2':
            read_entries()
        elif choice == '3':
            print("Exiting Personal Diary")
            break
        else: 
            print("Invvalid choice. Please try again")


personal_diary_app()