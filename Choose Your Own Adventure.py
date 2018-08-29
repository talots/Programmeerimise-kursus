# Imports time module to use sleep function between sentences
import time


# If the player chose 1 for their answer.
def choice_1_1():
    print("Vaatad ümberringi ja näed kolme puud mis on ööbimiseks kõlblikud,\nkuid igal puul on midagi häda.")
    time.sleep(1)
    print("Millise puu valid?")
    time.sleep(.5)
    while True:
        try:
            choice = int(input("1. puu on hästi madal\n2. puu all on teravad kivid\n3. ehituselt perfektne, kuid pead sängi jagama papagoiga\nValik: "))
        except ValueError:
            print("Palun sisestage vastus numbrites.")
            continue
        break
    if choice == 1:
        time.sleep(.8)
        print("Vee tõustes sai sinu taguots märjaks, mis segas und ja tegi olemise ebamugavaks.")
        time.sleep(.5)
        print("Mäng läbi!")

    elif choice == 2:
        time.sleep(.8)
        print("Kukkumishirm takistas magama jäämist, unest võisid ainult und näha.")
        time.sleep(.5)
        print("Mäng läbi!")

    elif choice == 3:
        time.sleep(.8)
        print("Papagoi ei lõpetanud kaagutamist, tukkumine ebaõnnestus.")
        time.sleep(.5)
        print("Mäng läbi!")

    else:
        print("Sisestasite numbri, mida valikutes ei ole, mängu lõpp...")


# If the player chose 2 for their answer.
def choice_1_2():
    print("Lageda taeva all magades tulid öösel saare asukad sind uurima,\nühine keel puudub, kuid midagi peab ütlema.")
    time.sleep(1)
    print("Millise vastuse esitad?")
    time.sleep(.5)
    while True:
        try:
            choice = int(input("1. hello, i come in peace\n2. sõnade asemel tõstad rahulikult käed\n3. yeet!\nValik: "))
        except ValueError:
            print("Palun sisestage vastus numbrites.")
            continue
        break
    if choice == 1:
        time.sleep(.8)
        print("Asukad mõistsid, et oled tulnukas, sind küpsetati lõkke kohal hommikusöögiks.")
        time.sleep(.5)
        print("Mäng läbi!")

    elif choice == 2:
        time.sleep(.8)
        print("Asukad mõistsid, et võtad ühendust jumalaga, kuid nemad olid ateistid,\nsind küpsetati lõkke kohal hommikusöögiks.")
        time.sleep(.5)
        print("Mäng läbi!")

    elif choice == 3:
        time.sleep(.8)
        print("Asukate suunurgad tõusid kõrgemale kui bitcoini hind 2017. aasta detsembris,\nsind kostitati nii söögi/joogi ja ööbimikohaga.")
        time.sleep(.5)
        print("Mäng läbi!")

    else:
        print("Sisestasite numbri, mida valikutes ei ole, mängu lõpp...")


# If the player chose 3 for their answer.
def choice_1_3():
    print("Lennukis on soe ja mugav ning leiad ühe piloodi taskust ka mp3 mängija.")
    time.sleep(1)
    print("Millist laulu magama jäämiseks kuulad?")
    time.sleep(.5)
    while True:
        try:
            choice = int(input("1. lofi hip hop radio - beats to relax/study to\n2. Kalevi mehed - Aurik Viljandist\n3. Vaiko Eplik & Eliit - Veel 15 Minutit Sessiooni Lõpuni\nValik: "))
        except ValueError:
            print("Palun sisestage vastus numbrites.")
            continue
        break
    if choice == 1:
        time.sleep(.8)
        print("Tuli välja, et tegu on väga pika lauluga, jäid magama olles tüdinenud.")
        time.sleep(.5)
        print("Mäng läbi!")

    elif choice == 2:
        time.sleep(.8)
        print("See laul oli nii catchy, et kuulasid seda tantsides terve öö.")
        time.sleep(.5)
        print("Mäng läbi!")

    elif choice == 3:
        time.sleep(.8)
        print("Pärast 15 minutit magasid nagu väike ingel.")
        time.sleep(.5)
        print("Mäng läbi!")

    else:
        print("Sisestasite numbri, mida valikutes ei ole, mängu lõpp...")


# First things you see when running the script. First part of the story.
def start_game():
    print("Oled sattunud lennuõnnetuse tõttu ainsa ellujääjana üksikule saarele.")
    time.sleep(1)
    print("Sul on valida kolme erineva koha vahel, kus veedad oma öö:")
    time.sleep(.8)
    # Gets input about the choice that player picks.
    while True:
        try:
            choice = int(input("1. puu otsas\n2. lageda taeva all\n3. lennuki alles jäänud kokpitis\nValik: "))
        except ValueError:
            print("Palun sisestage vastus numbrites.")
            continue
        break
    if choice == 1:
        time.sleep(.8)
        choice_1_1()

    elif choice == 2:
        time.sleep(.8)
        choice_1_2()

    elif choice == 3:
        time.sleep(.8)
        choice_1_3()

    else:
        print("Sisestasite numbri, mida valikutes ei ole, mängu lõpp...")


# If this is the main script that runs, it starts the game
if __name__ == "__main__":
    start_game()