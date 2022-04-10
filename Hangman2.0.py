from json.tool import main
import random

def hangman():
    country=['india1947','canada1982','bulgaria1908','chile1810','china1949','philippies1898','korea1945','denmark1945','maldives1965','ireland1916']
    word=random.choice(country)
    turns=15
    guessmade=''
    valid_entry=set("abcdefghijklmnopqrstuvwxyz012356789")

    while len(word)>0:

        #To create a dashed word in beginning
        main_word=''
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "
        
        if main_word==word:
            print(word)
            print("CONGRATS !! YOU WON ")
            break
        
        print("Guess the word ", main_word)
        guess=input()

        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("Enter a valid character: ")
            guess=input()

        if guess not in word:
            turns=turns-1
            if turns==14:
                print("turns left = ",turns)
            if turns==13:
                print("turns left = ",turns)
            if turns==12:
                print("turns left = ",turns)
            if turns==11:
                print("turns left = ",turns)
            if turns==10:
                print("turns left = ",turns)

            if turns==9:
                print("9 turns left !!")
                print("------")
            if turns==8:
                print("8 turns left !!")
                print("-------")
                print("   O   ")
            if turns==7:
                print("7 turns left !!")
                print("-------")
                print("   O   ")
                print("   |   ")
            if turns==6:
                print("6 turns left !!")
                print("-------")
                print("   O   ")
                print("   |   ")
                print("  /    ")
            if turns==5:
                print("5 turns left !!")
                print("-------")
                print("   O   ")
                print("   |   ")
                print("  / \  ")
            if turns==4:
                print("4 turns left !!")
                print("-------")
                print("  \O   ")
                print("   |   ")
                print("  / \  ")
            if turns==3:
                print("3 turns left !!")
                print("-------")
                print("  \O/  ")
                print("   |   ")
                print("  / \  ")
            if turns==2:
                print("2 turns left !!")
                print("-------")
                print("  \O/ |")
                print("   |   ")
                print("  / \  ")
            if turns==1:
                print("1 turns left !! Hangman on his last breath")
                print("-------")
                print("  \O/_|")
                print("   |   ")
                print("  / \  ")
            if turns==0:
                print("YOU LOOSE !!")
                break  


name=input("Enter your name: ")
print("WELCOME ",name," !!!")
print("Try to guess the country and its independent year in less than 15 attempts! (ex:iceland1944)")
print("------------------------------------------------")
hangman()
