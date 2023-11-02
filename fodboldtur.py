# IMPORTING PICKLE - I DONT EVEN LIKE PICKLES :(
import pickle

# IMPORTING COLORAMA (FARVE LIBRARY)
from colorama import Fore, init

init(autoreset=True)

filename = 'dict/betalinger.pk'

fodboldtur = {}


# FUNKTION DER GEMMER BELØB OG UPDATER DICT
def gem():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()


# FUNKTION DER INDEHOLDER INFORMATION OMKRING TUREN OG BETALINGEN
def information():
    total = sum(fodboldtur.values())
    print(Fore.LIGHTMAGENTA_EX + "\nHer er lidt information omkring turen!")
    print(f"\nTil denne fodboldtur skal der betales 4500 kr\n"
          f"Der er lige nu betalt {total} ud af 4500 kr")

    if total >= 4500:
        print(Fore.GREEN + "\nSheesh god tur, y'all are good to go!!!")
    else:
        print(Fore.RED + "\nPoor motherfuckers smh!!!")

    menu()


# FUNKTION DER PRINTER LISTEN/DICT SOM STATUS OVER HVOR MEGET DE FORSKELLIGE HAR BETALT
def printliste():
    print(Fore.LIGHTYELLOW_EX + " \nHer er listen over hvor meget de forskellige personer har betalt\n")

    for item in fodboldtur.items():
        print(item)

    menu()


# FUNKTION DER TAGER I MOD BETALINGER FRA BRUGEREN
def indbetal():
    print(Fore.LIGHTBLUE_EX + "\nDe valgte at indbetale et beløb\n")

    maxBeløb = 562.5
    navn = input("Skriv venligst deres fulde navn: ")

    if navn in fodboldtur.keys():
        beløb = fodboldtur[navn]

        while True:
            if beløb < maxBeløb:
                nytBeløb = input("\nIndtast beløb, som de ønsker at betale: ")
                nytBeløb = float(nytBeløb)
                if nytBeløb > 0:
                    if beløb + nytBeløb > maxBeløb:
                        print(Fore.RED + f"\nDe kan ikke betale mere end {maxBeløb - beløb} kr!")
                        break
                    else:
                        fodboldtur[navn] += nytBeløb
                        print(Fore.GREEN + "\nDeres betaling var succesfuld!")
                        break
                    if beløb == maxBeløb:
                        print(Fore.GREEN + f"\nDe kan ikke betale mere, da de allerede har betalt {beløb} kr")
                        break
                else:
                    print(Fore.RED + f"\nDe kan ikke betale et negativt beløb {nytBeløb}. Prøv igen!")
        else:
            print(Fore.GREEN + f"\nDe kan ikke betale mere, da de allerede har betalt {beløb} kr")
    else:
        print(Fore.RED + "\nNavnet de har angivet eksisterer ikke, prøv igen!")
        indbetal()

    menu()


def fjernBeløb():
    print(Fore.LIGHTBLUE_EX + "\nDe valgte at fjerne et beløb\n")

    minBeløb = 0
    navn = input("Skriv venligst deres fulde navn: ")

    if navn in fodboldtur.keys():
        beløb = fodboldtur[navn]

        while True:
            if beløb > minBeløb:
                nytBeløb = input("\nIndtast beløb, som de ønsker at fjerne: ")
                nytBeløb = float(nytBeløb)
                if nytBeløb > 0:
                    if beløb - nytBeløb < minBeløb:
                        print(Fore.RED + f"\nDe kan ikke fjerne mere end {beløb} kr!")
                        break
                    if nytBeløb == minBeløb:
                        print(Fore.RED + "\nDe kan ikke fjerne 0 kr fra deres betiling")
                    else:
                        fodboldtur[navn] -= nytBeløb
                        print(Fore.GREEN + f"\nDer er nu fjernet {nytBeløb} kr fra deres betaling!")
                        break
                else:
                    print(Fore.RED + f"\nDe kan ikke betale et negativt beløb {nytBeløb}. Prøv igen!")
        else:
            print(Fore.GREEN + f"\nDe kan ikke betale mere, da de allerede har betalt {beløb} kr")
    else:
        print(Fore.RED + "\nNavnet de har angivet eksisterer ikke, prøv igen!")
        indbetal()

    menu()


# FUNKTION DER FINDER DE TRE DER MANGLER AT BETALE MEST
# fik hjælp til lambda-funktionen af christoffer B-)
def hvemManglerMest():
    print(Fore.LIGHTMAGENTA_EX + "\nHer er de tre personer der har betalt mindst:\n")

    # finder elementerne i fodboldtur, sorterer dem efter størrelse og finder de keys med de tre laveste values
    elementer = list(fodboldtur.items())
    elementer.sort(key=lambda x: x[1])
    treLavesteVærdier = elementer[:3]

    # printer navne og beløb på tre der har betalt mindst
    for key, value in treLavesteVærdier:
        beløbMangler = 562.5 - value
        print(f"NAVN: {key} | BELØB: {value} kr | MANGLER: {beløbMangler} kr")

    print(Fore.LIGHTYELLOW_EX + "\nI må hellere snart se at få betalt jeres del!")

    menu()


# FUNKTION TIL HVIS BRUGEREN VÆLGER ET UGYLDIGT TAL
def ugyldigValg():
    print(Fore.RED + "\nUgyldigt valg. Skriv enten 1, 2, 3, 4, 5 eller 6, prøv igen!")

    menu()


# MENU FUNKTIONEN
def menu():
    gem()

    # printer menuens indhold
    print(Fore.LIGHTCYAN_EX + "\nMAIN MENU\n")
    print("1. Status over indbetalinger")
    print("2. Lav en indbetaling")
    print("3. Fjern et indbetalt beløb")
    print("4. Se hvem der mangler at betale mest")
    print("5. Information omkring turen")
    print("6. Afslut programmet")

    # gemmer brugerens valg i en "valg" (NOTE : default datatype for input er string)
    valg = input(Fore.LIGHTCYAN_EX + "\nIndtast deres valg: ")

    match valg:
        case "1":
            printliste()
        case "2":
            indbetal()
        case "3":
            fjernBeløb()
        case "4":
            hvemManglerMest()
        case "5":
            information()
        case "6":
            print(Fore.LIGHTYELLOW_EX + "\nProgrammet er nu afsluttet!")
        case _:
            ugyldigValg()

    gem()


infile = open(filename, "rb")
fodboldtur = pickle.load(infile)
infile.close()
menu()
