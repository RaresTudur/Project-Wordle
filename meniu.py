from os import system
from bot import wordle_bot
from game_console import wordle
from termcolor import cprint

alegere = -1

def meniu():

    cprint("---JOC WORDLE---", "grey","on_red",attrs=["bold", "underline"])
    cprint("1.JOCUL DE WORDLE OBISNUIT","white","on_red",attrs=["underline"])
    cprint("2.BOTUL DE WORDLE","white","on_red",attrs=["underline"])
    cprint("IESI DIN JOCUL DE WORDLE(orice tasta)","white","on_red",attrs=["underline"])

while alegere!=0:
    meniu()
    alegere=int(input())
    if alegere == 1:
        system('cls')
        wordle()
    elif alegere == 2:
        system('cls')
        wordle_bot()
    else:
        system('cls')
        print("La revedere!")
        break