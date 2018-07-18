buf = []
while True:
    line = input("Submit a value: ")
    if line == "SAVE":
        with open("97_ans.txt", "a+") as file:
            for el in buf:
                file.write(el + "\n")
        buf = []
    elif line == "CLOSE":
        file.close()
        break
    else:
        buf.append(line)
