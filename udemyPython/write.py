import string;
with open("letters.txt", "w") as f:
  for letter in string.ascii_lowercase:
    f.write(letter + "\n")
