
from random import randint
from random import choice
import random
import time
import sys

draw = {1: 
    ("_____ \n"
    "| \n"
    "| \n"
    "| \n"
    "| \n"),
     2:
    ("_____ \n"
    "|     O\n"
    "| \n"
    "| \n"
    "| \n"),
    3:
    ("_____ \n"
    "|     O\n"
    "|     |\n"
    "| \n"
    "| \n"),
     4:
    ("_____ \n"
    "|     O\n"
    "|    /|\ \n"
    "| \n"
    "| \n"),
     5:
    ("_____ \n"
    "|     O\n"
    "|    /|\ \n"
    "|    / \ \n"
    "| \n")}

 
def choose():
    global real, c, d, turns, size, hint, guessed_lett, guessed_word
    real, c, d, turns, size, hint = 0, 0, 0, 0, 0, 0 
    guessed_lett = []
    guessed_word = []
    fruit = ['apple', 'banana', 'cherry', 'grapes', 'pomegranate', 'pineapple', 'strawberry', 'watermelon', 'olive', 'raspberry']
    adj = ['adorable', 'dizzy', 'selfish', 'elegant', 'splendid', 'magnificent', 'fierce', 'obnoxious', 'grumpy', 'proud']
    country = ['france', 'malaysia', 'iceland', 'egypt', 'hungary', 'norway', 'philippines', 'thailand', 'california']
    fast_food = ['pastry', 'cookies', 'brownie', 'candies', 'burgers', 'macaroni', 'waffles', 'noodles']
    a = [fruit, adj, fast_food, country]
    name = ["Fruit", "Adjective", "Fast Food", "Country"]
    hint = ""
    real = (choice(choice(a)))
    size = len(real)
    if real in fruit :
        hint = name[0]
    elif real in adj :
        hint = name[1]
    elif real in fast_food :
        hint = name[2]
    elif real in country :
        hint = name[3]
    real = real.upper()
    c = 0
    turns = 5
    d = '-' * size

name = input("hey, what's your name? ").upper() 
time.sleep(0.5)
print('Hello', name ,'! Welcome to HANGMAN game! \n')
while True:
    time.sleep(0.5)
    a = input('''Type 'y' to play the game or 'n' if you don't want to.''').lower()
    if a=='n':
        time.sleep(1)
        print('\n')
        print("Hope we'll meet soon", name,":)")
        sys.exit()
    if a=='y':
        time.sleep(1)
        print('\n')
        print("Hope you're good in guessing words! Let's get started...")
        break
    else:
        print("that's not a valid input. please type 'y' or 'n'")
        continue


def guess():    
    print("\nTotal chances in the game are", turns)
    time.sleep(1)
    print("\nthe length of the word is" , size)
    for i in range(0,size):
        print("-" , end = ' ')
    time.sleep(0.5)
    print("HINT - ", hint) 
    
def game(c,d):
    global z
    time.sleep(0.8)
    lett = input("\nGUESS A LETTER OR THE WORD:").upper()
    if len(lett) == 1 and lett.isalpha():
        if lett in guessed_lett :
            print("You have already guessed this letter\n")
            guessed_lett.append(lett)
            return game(c,d)
        elif lett not in real :
            c = c + 1
            guessed_lett.append(lett)
            if c == 1:
                time.sleep(1)
                print("\nUH-OH... That's a wrong guess.\n" + str(turns - c) + " guesses remaining")
                print(draw[1])
                return game(c,d)
            elif c == 2:
                time.sleep(1)
                print("\nOOPS... Let's make a move again.\n" + str(turns - c) + " guesses remaining")
                print(draw[2])
                return game(c,d)
            elif c == 3:
                time.sleep(1)
                print("\nNOOOO... That's not the right one.\n" + str(turns - c) + " guess remaining")
                print(draw[3])
                return game(c,d)
            elif c == 4:
                time.sleep(1)
                print("\nWrong move AGAIN! You can do it...\n" + str(turns - c) + " guess remaining")
                print(draw[4])
                return game(c,d)
            elif c == 5:
                time.sleep(1)
                print("\nOh no.. BETTER LUCK NEXT TIME. The hangman got hanged :(\n")
                print(draw[5])
                time.sleep(0.5)
                print("The word was :" , real)
                print('''\nyou wanna strike a new word?''')
                z = input("Y/N :").upper()
                return z            
                                
        else :
            guess = lett
            guessed_lett.append(lett)
            if guess in real:
                for i in range(len(real)):
                    if lett==real[i]:
                        d = d[:i] + guess + d[i + 1:]
                print(d)
                if '-' not in d:
                    time.sleep(0.5)
                    print("HURRAYY!!! You saved the hangman! :) Good Job", name, ", you can be a detective")
                    print('''\nyou wanna strike a new word?''')
                    z = input("Y/N :").upper()
                    return z
                else:
                    print("YO, nice guess!\n")
                    return game(c,d)
                
    elif len(lett) == len(real) and lett.isalpha():
        if lett in guessed_word :
            print("You have already guessed this word")
            guessed_word.append(lett)
            return game(c,d)
        elif lett not in real :
            c = c + 1
            guessed_word.append(lett)
            if c == 1:
                time.sleep(1)
                print("\nUH-OH... That's a wrong guess.\n" + str(turns - c) + " guesses remaining")
                print(draw[1])
                return game(c,d)
            elif c == 2:
                time.sleep(1)
                print("\nOOPS... Let's make a move again.\n" + str(turns - c) + " guesses remaining")
                print(draw[2])
                return game(c,d)
            elif c == 3:
                time.sleep(1)
                print("\nNOOOO... That's not the right one.\n" + str(turns - c) + " guess remaining")
                print(draw[3])
                return game(c,d)
            elif c == 4:
                time.sleep(1)
                print("\nWrong move AGAIN! You can do it...\n" + str(turns - c) + " guess remaining")
                print(draw[4])
                return game(c,d)
            elif c == 5:
                time.sleep(1)
                print("\nOh no.. BETTER LUCK NEXT TIME. The hangman got hanged :(\n")
                print(draw[5])
                time.sleep(0.5)
                print("The word was :" , real)
                print('''\nyou wanna strike a new word?''')
                z = input("Y/N :").upper()
                return z
                
        else :
            print("HURRAYY!!! You saved the hangman! :) Good Job", name, ", you can be a detective")
            print('''\nyou wanna strike a new word?''')
            z = input("Y/N :").upper()
            return z
            return game(c,d)

    else :
        print("that's not a valid guess")
        return game(c,d)
        
    if '-' not in d:
        time.sleep(0.5)
        print("HURRAYY!!! You saved the hangman! :) Good Job", name, ", you can be a detective")
        print('''\nyou wanna strike a new word?''')
        z = input("Y/N :").upper()
        return z

run = True

if __name__ == "__main__":
    while run:
        choose()
        guess()
        game(c,d)
        if z == 'N':
            run = False
    print("Thankyou for playing ;)")