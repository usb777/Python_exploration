f = open("create.txt", "a")
f.write("Woops! I have deleted the content!")
f.close()

f = open("create.txt", "r")
print(f.read())
