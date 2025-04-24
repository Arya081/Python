with open("main.txt", "r") as main, open("aim.txt", "w") as aim:
    for line in source:
        aim.write(line.upper())
