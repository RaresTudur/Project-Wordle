import random
import os
from termcolor import colored


def ghicire(raspuns_corect,cuvant_incercat):
    pozitie = 0
    global hint
    hint = ""
    cuvant = ""
    for l in cuvant_incercat:
        if l == raspuns_corect[pozitie]:
            hint += "C"
            cuvant += colored(l,'green')
        elif l in raspuns_corect:
            hint += "E"
            cuvant += colored(l,'yellow')
        else:
            hint += "-"
            cuvant += colored(l,'grey')
        pozitie += 1
    print(cuvant)
    return hint == "CCCCC"

def citire_dictionar():
    fisier_dictionar = open("cuvinte_wordle.txt",'r')
    continut = fisier_dictionar.read()
    global dictionar
    dictionar = continut.split()
    fisier_dictionar.close()
    

def wordle():
    citire_dictionar()
    raspuns_corect = random.choice(dictionar)
    numar_incercari = 0
    cuvantul_este_ghicit = False
    while cuvantul_este_ghicit != True:
        cuvant_incercat = input("Introdu ce cuvant crezi ca am ales ")
        os.system('cls')
        if(len(cuvant_incercat) != 5):
            print("Cuvantul introdus nu are 5 litere.")
            print("Te rog incearca din nou",sep = "\n")
            cuvant_incercat = input()
            cuvant_incercat = cuvant_incercat.upper()
            os.system('cls')
        if(cuvant_incercat not in dictionar):
            print("Cuvantul nu exista in lista de cuvinte")
            print("Incearca din nou!")
            cuvant_incercat = input()
            cuvant_incercat = cuvant_incercat.upper()
            os.system('cls')
        cuvant_incercat = cuvant_incercat.upper()
        print(cuvant_incercat)
        numar_incercari += 1
        cuvantul_este_ghicit = ghicire(raspuns_corect,cuvant_incercat)
    if cuvantul_este_ghicit == True:
        print(f"Bravo! Ai ghicit cuvantul din {numar_incercari} incercari")

wordle()