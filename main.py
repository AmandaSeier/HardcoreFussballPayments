import pickle

filename = 'dict/betalinger.pk'

fodboldtur = {}


# FUNKTION DER AFSLUTTER PROGRAMMET
def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!") # printer at programmet er afsluttet


# FUNKTION DER PRINTER LISTEN/DICT MED
def printliste():
    for item in fodboldtur.items():
        print(item) # tjekker alle elementerne i dict og printer dem
    menu() # kalder funktionen menu


# FUNKTION DER TAGER I MOD BETALINGER FRA BRUGEREN
def indbetal():
    navn = input("Navn: ") # spørger brugeren om deres navn

    if navn in fodboldtur.keys(): # hvis brugerens navn eksisterer i dict bliver de spurgt om beløb
        beløb = input("Indtast beløb, som du ønsker at betale: ")
        beløb = int(beløb)

    else: # står det ikke i dict printes dette til terminalen
        print("Navnet du har skrevet findes ikke, prøv igen")
        indbetal() # kalder funktionen menu


# FUNKTION DER PRINTER NAVNE PÅ DE TRE PERSONER DER MANGLER AT BETALE MEST
def hvemManglerMest():
    pass


# MENU FUNKTIONEN
def menu():
    # printer menuens indhold
    print("MENU")
    print("1 : Oversigt over betalte beløb")
    print("2 : Lav en indbetaling")
    print("3 : Se hvem der mangler at betale mest")
    print("4 : Afslut programmet ")

    # gemmer brugerens valg i en variabel
    valg = input("Indtast dit valg:")

    # den gemte værdi bruges i denne match case, alt efter hvad brugeren skrev vil følgende funktioner kaldes
    match valg:
        case "1":
            printliste() # funktionen printListe kaldes
        case "2":
            indbetal() # funktionen indbetal kaldes
        case "3":
            hvemManglerMest() # funktionen hvemManglerMest kaldes
        case "4":
            afslut() # funktionen afslut kaldes
        case _: # hvis valget er ugyldigt vil denne meddelelse printes
            print("Ugyldigt valg. Skriv enten 1, 2, 3 eller 4, prøv igen!")
            menu() # kalder funktionen menu


infile = open(filename, "rb")
fodboldtur = pickle.load(infile)
infile.close()
menu()
