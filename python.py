words = []
def main():
    while True:
        choose = input("\nA)Add Word \nB)Sort \nC)Reverse Sort \nD)Clear \nE)Length of Array \nF)Exit \n\nPlease enter a letter from the above: ").upper()
        if choose == "A":
            word = input("\nPlease enter a word: ")
            words.append(word)
            print()
            [print(i) for i in words]
        elif choose == "B":
            words.sort()
            [print(i) for i in words]
        elif choose == "C":
            words.reverse()
            [print(i) for i in words]
        elif choose == "D":
            words.clear()
            [print(i) for i in words]
        elif choose == "E":
            print('\n{0}\n'.format(len(words)))
            [print(i) for i in words]
        elif choose == "F":
            exit()
        else:
            continue
