user_string = input("Please input a string. ")
empty = ""
for letters in range(len(user_string) - 1, -1, -1):
    empty += user_string[letters]


print(empty)

