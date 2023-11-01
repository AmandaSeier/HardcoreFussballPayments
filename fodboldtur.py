# IMPORTING PICKLE - I DONT EVEN LIKE PICKLES :(
import pickle
from colorama import Fore, init

init(autoreset=True)

filename = 'dict/betalinger.pk'

fodboldtur = {}


# FUNKTION DER GEMMER BELØB OG UPDATER DICT
def gem():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()


# FUNKTION DER INDEHOLDER INFORMATION OMKRING TUREN
def information():
    total = sum(fodboldtur.values())
    print(Fore.LIGHTMAGENTA_EX + "\nHer er lidt information omkring turen!")
    print(f"\nTil denne tur skal der betales 4500 kr i alt \n"
          f"Der er lige nu betalt {total} ud af 4500 kr")

    if total >= 4500:
        print(Fore.GREEN + "\nSheesh god tur, y'all are good to go!!!")
    else:
        print(Fore.RED + "\nPoor motherfuckers smh!!!")

    menu()


# FUNKTION DER PRINTER LISTEN/DICT SOM STATUS OVER HVOR MEGET DE FORSKELLIGE HAR BETALT
def printliste():
    print(Fore.LIGHTYELLOW_EX + " \nHer er listen over hvor meget de forskellige personer har betalt \n")

    for item in fodboldtur.items():
        print(item)

    menu()


# FUNKTION DER TAGER I MOD BETALINGER FRA BRUGEREN
def indbetal():
    print(Fore.LIGHTBLUE_EX + "\nDe valgte at indbetale et beløb\n")

    maxBeløb = 562.5
    navn = input("Deres fulde navn: ")

    if navn in fodboldtur.keys():
        beløb = fodboldtur[navn]
        if beløb < maxBeløb:
            nytBeløb = input("\nIndtast beløb, som de ønsker at betale: ")
            nytBeløb = float(nytBeløb)
            if nytBeløb > 0:
                if beløb + nytBeløb > maxBeløb:
                    print(f"\nDe kan ikke betale mere end {maxBeløb - beløb} kr!")
                else:
                    fodboldtur[navn] += nytBeløb
                    print("\nDeres betaling var succesfuld!")
                if beløb >= maxBeløb:
                    print(f"\nDe kan ikke betale mere, da de allerede har betalt {beløb} kr")
            else:
                print(f"\nDe kan ikke betale et negativt beløb {nytBeløb}. Prøv igen!")
        else:
            print(f"\nDe kan ikke betale mere, da de allerede har betalt {beløb} kr")
    else:
        print("\nNavnet de har angivet eksisterer ikke, prøv igen!")
        indbetal()

    menu()


# FUNKTION DER KAN FJERNE PENGE FRA EN PERSON
def fjernBeløb():
    print(Fore.LIGHTYELLOW_EX + "\nDe ønsker at fjerne penge fra en indbetaling")

    navn = input("\nHvem ønsker de at fjerne et beløb fra: ")

    if navn in fodboldtur.keys():
        beløb = None
        while beløb is None or beløb < 0:
            beløb_input = input("\nHvor meget ønsker de at fjerne: ")
            try:
                beløb = int(beløb_input)
                if beløb < 0:
                    print(Fore.RED + "\nHovsa, det indtastede beløb er negativt! Prøv igen")
            except ValueError:
                print("\nIndtast venligst et gyldigt heltal for beløbet.")
    else:
        print("\nNavnet de har skrevet findes ikke, prøv igen")
        fjernBeløb()
        return

    fodboldtur[navn] -= beløb

    menu()


# FUNKTION DER PRINTER NAVNE PÅ DE TRE PERSONER DER MANGLER AT BETALE MEST
# btw med lidt hjælp fra dem der christoffer der, ham den seje du ved nok B-)
def hvemManglerMest():
    print(Fore.LIGHTMAGENTA_EX + "\nHer er de tre personer der har betalt mindst \n")

    elementer = list(fodboldtur.items())
    elementer.sort(key=lambda x: x[1])
    treLavesteVærdier = elementer[:3]

    # printer navne og beløb på tre der har betalt mindst
    for key, value in treLavesteVærdier:
        print(f"NAVN: {key} | BELØB: {value}")

    menu()


# FUNKTION TIL HVIS BRUGEREN VÆLGER ET UGYLDIGT TAL
def ugyldigValg():
    print(Fore.RED + "\nUgyldigt valg. Skriv enten 1, 2, 3 eller 4, prøv igen!")

    menu()


# MENU FUNKTIONEN
def menu():
    gem()

    # printer menuens indhold
    print(Fore.LIGHTCYAN_EX + "\nMENU\n")
    print("1   Status over indbetalinger")
    print("2   Lav en indbetaling")
    print("3   Fjern et indbetalt beløb")
    print("4   Se hvem der mangler at betale mest")
    print("5   Information omkring turen")
    print("6   Afslut programmet")

    # gemmer brugerens valg i en variabel (NOTE : default datatype for input er string)
    valg = input(Fore.GREEN + "\nIndtast deres valg: ")

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
            print(Fore.GREEN + "\nProgrammet er nu afsluttet!")
        case _:
            ugyldigValg()

    gem()


infile = open(filename, "rb")
fodboldtur = pickle.load(infile)
infile.close()
menu()
