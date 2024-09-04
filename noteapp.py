"""
Name: noteapp.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Homework #8
Task: File Input and Output (I/O)
"""
import os.path


def read_file(file_name):
    with open(file_name, "r") as oldFile:
        all_notes = oldFile.read()
        print(all_notes)
        return False


def write_file(file_name):
    with open(file_name, "w") as oldFile:
        print("Hit 'enter' after typing to add a new line")
        print("Type 'exit' to finish adding notes")
        while True:
            content = input("content: ")
            if content == "exit":
                break
            else:
                oldFile.write(str(content)+"\n")
                print("Notes added. Continue or type 'exit' to close")


def append_to_file(file_name):
    with open(file_name, "a") as oldFile:
        print("Hit 'enter' after typing to add a new line")
        print("Type 'exit' to finish adding notes")
        while True:
            content = input("content: ")
            if content == "exit":
                break
            else:
                oldFile.write(str(content)+"\n")
                print("Notes added. Continue or type 'exit' to close")


def replace_single_line(file_name, line):
    oldFile = open(file_name, "r")
    all_lines = oldFile.readlines()
    content = input("content: ")
    all_lines[line - 1] = str(content) + "\n"
    oldFile = open(file_name, "w")
    oldFile.writelines(all_lines)
    print(f"Line {line} updated\n")


print("====== Welcome to the Note Taker (c)2020 Banky====")
print("Create, Read, Update and Delete Notes")

while True:
    file_name = input(
        "Please enter a file name for your notes ('E' to exit): \n")
    if file_name == "E":
        break
    menu_list = ["A", "B", "C", "D", "E"]
    option = ""

    if os.path.exists(file_name):
        print(f"'{file_name}' already exists")
        print("what would you like to do? ")
        print(" [A]. Read the file")
        print(" [B]. Delete the file and start over")
        print(" [C]. Append to the file")
        print(" [D]. Replace a Single Line")
        print(" [E]. Exit the program")
        option = input("Please select an option (A, B, C, D, E): \n")
        option = option.upper()

        while option not in menu_list:
            print("Invalid option: Select from option below")
            print(" [A]. Read the file")
            print(" [B]. Delete the file and start over")
            print(" [C]. Append to the file")
            print(" [D]. Replace a Single Line")
            print(" [E]. Exit the program")
            option = input("Please select an option(A, B, C, D, E): \n")
            option = option.upper()
        if option == "A":
            # Read file function
            print(f"You selected {option}: Read the file")
            print("\n***** File Contents ******")
            read_file(file_name)
            print("----- End of Contents -----\n")
        elif option == "B":
            print(f"You selected {option}: Delete File and Start Over")
            write_file(file_name)
            # Open file in write mode
            print(f"All notes written to the file '{file_name}'\n")
        elif option == "C":
            print(f"You selected {option}: Append to the file")
            append_to_file(file_name)
            # Open the file in append mode
            print(f"All notes appended to the file '{file_name}'\n")
        elif option == "D":
            print(f"You selected {option}: Write to Specific Line")
            fileToEdit = open(file_name, "r")
            all_lines = fileToEdit.readlines()
            no_of_lines = len(all_lines)
            for i in range(no_of_lines):
                print(f"{i+1}. {all_lines[i]}", end="")
            # print(all_lines, no_of_lines)
            print(f"\nThere are {no_of_lines} lines in the file")
            while True:
                line_to_write = input(
                    f"which line would you like to change(1 - {no_of_lines})?\n")
                try:
                    line_to_write = int(line_to_write)
                except ValueError:
                    print("You didn't enter a valid Value\n")
                    continue
                else:
                    line_to_write = int(line_to_write)
                    break
            while (line_to_write > no_of_lines) or (line_to_write <= 0):
                print(
                    f"Sorry, that line doesn't exist in the file.\nThe last line is line {no_of_lines}")
                line_to_write = int(input(
                    f"which line would you like to change(1 - {no_of_lines})[-1 to exit]?\n"))
                if line_to_write == -1:
                    break
                if line_to_write <= no_of_lines:
                    break
            replace_single_line(file_name, line_to_write)
        elif option == "E":
            break
        else:
            print(option)
    else:
        # Create a new file in append mode
        with open(file_name, "a") as new_file:
            print(f"New note - '{file_name}' - created")
            print("Hit 'enter' after typing to add a new line")
            print("Type 'exit' to finish adding notes")
            while True:
                content = input("content: ")
                if content == "exit":
                    break
                else:
                    new_file.write(str(content)+"\n")
                    print("Notes added. Continue or type 'exit' to close")

print("==== Thank you for using the Note Taker ====")
