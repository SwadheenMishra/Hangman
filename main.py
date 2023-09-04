'''
Made by- Swadheen Mishra
'''

import requests
from termcolor import colored

class man:
    HumanHang = {
                1: '''
                   O   
                ''',
            
               2: '''
                   O
                  /
                ''',

               3: '''
                   O
                  /|
                ''',

               4: '''
                   O
                  /|\ 
                ''',

              5: '''
                   O
                  /|\ 
                  /  
                ''',

               6: '''
                   O
                  /|\ 
                  / \ 
                ''',

                0: ''
                }


    def is_alive(self, numT: int, maxT: int) -> bool:
        return numT < maxT
    
    def output_man(self, numT: int) -> int:
        print(colored(self.HumanHang[numT], 'blue'))

def find_in_string(s: str, l: str) -> list:
    pos = []
    posCount = 0
    string = s.lower()
    letter = l.lower()

    for i in string:
        posCount += 1

        if i == letter:
            pos.append(posCount)

    return pos

def make_hintBox(Word: str) -> list:
    l = []

    for i in range(len(Word)):
        l.append('_')

    return l

def get_random_words(length: int) -> str:
    if length == 0:
        apiUrl = 'https://random-word-api.herokuapp.com/word'
    else:
        apiUrl = f'https://random-word-api.herokuapp.com/word?length={length}'
    
    word = requests.get(apiUrl).json()
    return (word[0]).lower()

def Start_game(length: int):
    password = 'byteclub123'

    maxTries = 6
    numTries = 0

    lettersTried = []

    running = True

    try:
        CorrectWord = get_random_words(length)
    except:
        print(colored('[-] Error! please check your internet connection', 'red'))
        exit(-1)

    WordHint = make_hintBox(CorrectWord)

    Man = man()

    while running:
        inputWords = ''.join(WordHint)
        Man.output_man(numTries)

        if inputWords == CorrectWord:
            print(colored('You Won!', 'green'))
            break
        elif Man.is_alive(numTries, maxTries):
            print(colored(inputWords, 'blue'))
            print(colored(f'Letters tried: {", ".join(lettersTried)}', 'blue'))

            letter = input(colored('Enter a letter: ', 'blue')).lower()

            if letter == password:
                print(CorrectWord)

            LetterPos = find_in_string(CorrectWord, letter)

            if LetterPos != []:
                for j in LetterPos:
                    WordHint[(j - 1)] = letter
            else:
                lettersTried.append(letter)
                numTries += 1
        else:
            print(colored(f'You lost! the word was {CorrectWord}', 'red'))
            break

def main():
    print(colored('''                                       
     _    _                                      
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                        __/ |                       
                        |___/                        
    >>>============================================<<<
 >>>=================By-Swadheen Mishra===============<<<
    >>>============================================<<<
        ''', 'blue'))

    while True:
        UserInput = input(colored('[+] Would you like to play the game? [y/n]: ', 'blue')).lower()

        if UserInput == 'y':
            WordLength = input(colored('[+] Enter the length of the word (leave it blank if you want it to be random): ', 'blue'))

            try:
                if WordLength != '' and WordLength != '1':
                    length = int(WordLength)
                else:
                    length = 0

                Start_game(length)

            except:
                print(colored('[-] Error! input a valid number!', 'red'))
        else:
            break
    


if __name__ == '__main__':
    main()
