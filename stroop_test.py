from __future__ import print_function
import colorama
import random
import sys

COLOR_DICTIONARY = {'BLACK' : colorama.Fore.BLACK , 'RED': colorama.Fore.RED, 'GREEN': colorama.Fore.GREEN, 'YELLOW':colorama.Fore.YELLOW, 'BLUE': colorama.Fore.BLUE, 'MAGENTA' : colorama.Fore.MAGENTA, 'CYAN' : colorama.Fore.CYAN , 'WHITE': colorama.Fore.WHITE}
#COLOR_LIST = ['BLACK' , 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']

if 'win' in sys.platform:
    #print('win')
    DEFAULT_BACKGROUND = 'BLACK'
    DEFAULT_FOREGROUND = 'WHITE'
else:
    DEFAULT_BACKGROUND = 'WHITE'
    DEFAULT_FOREGROUND = 'BLACK'
    
def randSeq(seq, color):
    randColor = random.choice(list(seq))
    if randColor == color:
        return randSeq(list(seq), list(color))
    else:
        return randColor

def main():
    if sys.version_info.major < 3:
        print("You're using a depreciated version of python! You really should update!")
    colorama.init()
    print(colorama.Fore.RESET + colorama.Back.RESET + colorama.Style.RESET_ALL)
    print("Assuming " + DEFAULT_BACKGROUND + " is the background color, and " + DEFAULT_FOREGROUND + " is the foreground color\n\n")
    correctAnswers = []
    for color in COLOR_DICTIONARY.keys():
        randColor = randSeq(COLOR_DICTIONARY.keys(), random.choice(list(COLOR_DICTIONARY.keys())))
        if (color != DEFAULT_BACKGROUND) and (color != randColor):
            print(COLOR_DICTIONARY[color] + randColor)
            correctAnswers.append(color)
    print()
    print(colorama.Fore.RESET + colorama.Back.RESET + colorama.Style.RESET_ALL)
    print('Correct Answers:')
    print(correctAnswers)


if __name__ == '__main__':
    main()