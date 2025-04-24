with open("main.txt", "r") as main, open("end.txt", "w") as end:
    for line in main:
        word = line.split()
        filter_word = [w for w in word if w.lower() not in ['a', 'the', 'an']]
        end.write(" ".join(filter_word) + "\n")
