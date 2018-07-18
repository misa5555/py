with open("urls.txt", "r") as file:
    lines = file.readlines()
print(lines)

with open("url_corrected.txt", "w") as file:
    for line in lines:
        line = line.replace("https", "http", 1)
        line =  line[:6] + '/' + line[6:-1] + "/\n" 
        file.write(line)
