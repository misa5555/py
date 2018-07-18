line = input("Enter values: ")
ary = line.split(",")

with open("user_data_comma95.txt", "w") as file:
    for el in ary:
        file.write(el + "\n", "w")
