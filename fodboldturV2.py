# IMPORTING PICKLE - I DONT EVEN LIKE PICKLES :(
import pickle

# IMPORTING COLORAMA (FARVE LIBRARY)
from colorama import Fore, init

init(autoreset=True)

filename = 'dict/betalinger.pk'
fodboldtur = {}

def load_data() -> dict:
    global fodboldtur
    infile = open(filename, "rb")
    fodboldtur = pickle.load(infile)
    infile.close()
    return fodboldtur

# FUNKTION DER GEMMER BELØB OG UPDATER DICT
def gem():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()

# FUNKTION DER TAGER I MOD BETALINGER FRA BRUGEREN
def indbetal(navn: str, nytBeløb: float):
    maxBeløb = 562.5

    if nytBeløb < 0:
        print(Fore.RED + f"\nDe kan ikke betale et negativt beløb {nytBeløb}. Prøv igen!")
        return

    if navn not in fodboldtur.keys():
        print(Fore.GREEN + f"\nDe kan ikke betale mere, da de allerede har betalt {beløb} kr")
        return

    beløb = fodboldtur[navn]

    if beløb == maxBeløb:
        print(Fore.GREEN + f"\nDe kan ikke betale mere, da de allerede har betalt {beløb} kr")
        return

    if beløb + nytBeløb > maxBeløb:
        print(Fore.RED + f"\nDe kan ikke betale mere end {maxBeløb - beløb} kr!")
        return

    fodboldtur[navn] += nytBeløb
    print(Fore.GREEN + "\nDeres betaling var succesfuld!")


# FUNKTION DER FINDER DE TRE DER MANGLER AT BETALE MEST
# fik hjælp til lambda-funktionen af christoffer B-)
def hvemManglerMest():
    print(Fore.LIGHTMAGENTA_EX + "\nHer er de tre personer der har betalt mindst:\n")

    # finder elementerne i fodboldtur, sorterer dem efter størrelse og finder de keys med de tre laveste values
    elementer = list(fodboldtur.items())
    elementer.sort(key=lambda x: x[1])
    treLavesteVærdier = elementer[:3]

    # printer navne og beløb på tre der har betalt mindst
    return treLavesteVærdier
