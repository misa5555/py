content = []
while True:

    line = input("Write a value: ")
    if line == "CLOSE":
        break
    content.append(line)

with open("96result.txt", "w") as file:
    for line in content:
        file.write(line + "\n")
