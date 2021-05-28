words = [] # A list of strings
def main():
    choose=input("\nA)Add Word \nB)Sort \nC)Reverse Sort \nD)Clear \nE)Length of Array \nF)Exit \n\nPlease enter a letter from the above: ").upper() # User gets to make a choice
    if choose=="A": # User chooses A and can enter a word and that will be added to the list
        word=input("\nPlease enter a word: ")
        words.append(word)
        print()
        [print(i) for i in words]
        main()
    elif choose=="B": # User chooses B and the list is sorted alphabetically and outputted
        words.sort()
        [print(i) for i in words]
        main()
    elif choose=="C": # User chooses C and the list is sorted in reverse and outputted
        words.reverse()
        [print(i) for i in words]
        main()
    elif choose=="D": # User chooses D and the list is cleared
        words.clear()
        [print(i) for i in words]
        main()
    elif choose=="E": # User chooses E and the length of the list is outputted
        print('\n{0}\n'.format(len(words)))
        [print(i) for i in words]
        main()
    elif choose=="F": # User chooses F and the program exits
        exit()
    else: # User doesn't make any of the above choices it will be repeated again
        main()
main()