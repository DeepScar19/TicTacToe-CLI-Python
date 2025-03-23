from time import sleep
import random
global felder

def felder_ausgeben():
    for i in range(3):
        print(felder[i*3] + " | " +felder[i*3+1] + " | " + felder[i*3+2] )

def zufalls_ecken():
    ecken = []
    for i in [0,2,6,8]:
        if felder[i] == str(i+1):
            ecken.append(i)

    return random.choice(ecken)

def zufalls_kanten():
    kanten = []
    for i in [1,3,5,7]:
        if felder[i] == str(i+1):
            kanten.append(i)
    return random.choice(kanten)

def prüfe_zumachen(player):
    for i in range(3):
        #Prüfe frei waagerecht links
        if felder[i*3+1] == player and felder[i*3+2] == player and felder[i*3] == str(i*3+1):
            return i*3
        #Prüfe frei waagerecht mitte
        elif felder[i*3] == player and felder[i*3+2] == player and felder[i*3+1] == str(i*3+2):
            return i*3+1
        #Prüfe frei waagerecht rechts
        elif felder[i*3] == player and felder[i*3+1] == player and felder[i*3+2] == str(i*3+3):
            return i*3+2    
        #Prüfe frei senkrecht unten
        elif felder[i] == player and felder[i+3] == player and felder[i+6] == str(i+7):
            return i+6
        #Prüfe frei senkrecht mitte
        elif felder[i] == player and felder[i+6] == player and felder[i+3] == str(i+4):
            return i+3
        #Prüfe frei senkrecht oben
        elif felder[i+3] == player and felder[i+6] == player and felder[i] == str(i+1):
            return i
    #Prüfe frei diagonal oben links unten rechts oben
    if felder[4] == player and felder[8] == player and felder[0] == "1":
        return 0
    #Prüfe frei diagonal oben links unten rechts mitte
    elif felder[0] == player and felder[8] == player and felder[4] == "5":
        return 4
    #Prüfe frei diagonal oben links unten rechts unten
    elif felder[0] == player and felder[4] == player and felder[8] == "9":
        return 8
    #Prüfe frei diagonal unten links oben rechts oben
    elif felder[4] == player and felder[6] == player and felder[2] == "3":
        return 2
    #Prüfe frei diagonal unten links oben rechts mitte
    elif felder[2] == player and felder[6] == player and felder[4] == "5":
        return 4
    #Prüfe frei diagonal unten links oben rechts unten
    elif felder[2] == player and felder[4] == player and felder[6] == "7":
        return 6

def ende_prüfung():
    gewonnen = False
    global Felder
     #Felder waagerecht
    for i in range(3):
        if felder[i*3] == felder[i*3+1] and felder[i*3+1] == felder[i*3+2]:
            print(f"Spieler {felder[i*3]} hat gewonnen!")
            gewonnen = True
        if felder[i] == felder[i+3] and felder[i] == felder[i+6]:
            print(f"Spieler {felder[i]} hat gewonnen!")
            gewonnen = True
    #Felder diagonal oben links unten rechts
    if felder[0] == felder [4] and felder[4] == felder[8]:
        print(f"Spieler {felder[0]} hat gewonnen!")
        gewonnen = True
    #Felder diagonal unten links oben rechts
    if felder[6] == felder [4] and felder[4] == felder[2]:
        print(f"Spieler {felder[6]} hat gewonnen!")
        gewonnen = True
    return gewonnen

def main():
    global felder
    computerplay = False
    while True:
        mode = input("Möchtest du gegen den Computer [c] oder gegen einen Menschen [m] spielen? ")
        if mode == "c":
            computerplay = True
            break
        elif mode == "m":
            computerplay = False
            break
        else:
            print("Gebe eine richtige Antwort ein!")
    felder = ["1","2","3","4","5","6","7","8","9"]
    spieler = "X"
    felder_ausgeben()
    ende = False
    while ende == False:
        if computerplay == False:
            print(f"Spieler {spieler} ist dran!")
            spielzug = input("Bitte ein Feld eingeben: ")
            while True:
                    if spielzug in felder and spielzug != "X" and spielzug != "0":
                        print("Spielzug: ", spielzug)
                        break
                    else:
                        print("Gebe eine gültige Zahl ein!")
                        spielzug = input("Bitte ein Feld eingeben: ")
            felder[int(spielzug)-1] = spieler
            if spieler == "X":
                spieler = "0"
            else:
                spieler = "X"
            felder_ausgeben()
            ende = True
            for i in ["1","2","3","4","5","6","7","8","9"]:
                if i in felder:
                    ende = False
            if ende == True:
                print("Unentschieden")
                break
            ende = ende_prüfung()
        else:
            if spieler == "X":
                print("Du (X) bist dran!")
                spielzug = input("Bitte ein Feld eingeben: ")
                while True:
                        if spielzug in felder and spielzug != "X" and spielzug != "0":
                            print("Spielzug: ", spielzug)
                            break
                        else:
                            print("Gebe eine gültige Zahl ein!")
                            spielzug = input("Bitte ein Feld eingeben: ")
                felder[int(spielzug)-1] = spieler
                felder_ausgeben()
                ende = True
                for i in ["1","2","3","4","5","6","7","8","9"]:
                    if i in felder:
                        ende = False
                if ende == True:
                    print("Unentschieden")
                    break
                spieler = "0"
            else:
                print("Der Computer (0) ist dran!")
                if "0" not in felder:
                    if felder[4] == "5":
                        felder[4] = "0"
                        print("Spielzug des Computers: 5")
                    else:
                        random_ecke = zufalls_ecken()
                        felder[random_ecke] = "0"
                        print("Spielzug des Computers:", random_ecke + 1)
                elif felder[0] == "X" and felder[8] == "X" and felder.count("0") == 1 or felder[2] == "X" and felder[6] == "X" and felder.count("0") == 1:
                    random_kante = zufalls_kanten()
                    felder[random_kante] = "0"
                    print("Spielzug des Computers:", random_kante + 1)
                elif prüfe_zumachen("0") != None:
                    print("Spielzug des Computers:", prüfe_zumachen("0") + 1)
                    felder[prüfe_zumachen("0")] = "0"
                elif prüfe_zumachen("X") != None:
                    print("Spielzug des Computers:", prüfe_zumachen("X") + 1)
                    felder[prüfe_zumachen("X")] = "0"
                else:
                    try:
                        random_ecke = zufalls_ecken()
                        felder[random_ecke] = "0"
                        print("Spielzug des Computers:", random_ecke + 1)
                    except:
                        random_kante = zufalls_kanten()
                        felder[random_kante] = "0"
                        print("Spielzug des Computers:", random_kante + 1)
                felder_ausgeben()
                ende = ende_prüfung()
                spieler = "X"
print("TicTacToe - Das Spiel")
print("-----------------------------\n")
ende = False
while ende == False:
    main()
    while True: #Weiterspielen-Abfrage
        weiterspielen = input("Möchtest du weiterspielen? [y/n]")
        if weiterspielen == "y":
            ende = False
            break
        elif weiterspielen == "n":
            print("TicTacToe wird beendet ", end = "", flush= True)
            for i in range(3):
                sleep(0.7)
                print(".", end = "", flush=True)
            ende = True
            sleep(3)
            print("\nTicTacToe beendet!")
            break
        else:
            print("Gebe eine richtige Antwort an!")