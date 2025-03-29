from time import sleep
import random

def print_fields(f):
    for i in range(3):
        print(f[i*3] + " | " + f[i*3+1] + " | " + f[i*3+2] )

def get_random_corner(f):
    corners = []
    for i in [0,2,6,8]:
        if f[i] == str(i+1):
            corners.append(i)
    return random.choice(corners)

def get_random_side(f):
    sides = []
    for i in [1,3,5,7]:
        if f[i] == str(i+1):
            sides.append(i)
    return random.choice(sides)

def check_close(player, f):
    for i in range(3):
        #Check open horizontal left
        if f[i*3+1] == player and f[i*3+2] == player and f[i*3] == str(i*3+1):
            return i*3
        #Check open horizontal mitte
        elif f[i*3] == player and f[i*3+2] == player and f[i*3+1] == str(i*3+2):
            return i*3+1
        #Check open horizontal rechts
        elif f[i*3] == player and f[i*3+1] == player and f[i*3+2] == str(i*3+3):
            return i*3+2    
        #Check open vertical bottom
        elif f[i] == player and f[i+3] == player and f[i+6] == str(i+7):
            return i+6
        #Check open vertical mitte
        elif f[i] == player and f[i+6] == player and f[i+3] == str(i+4):
            return i+3
        #Check open vertical top
        elif f[i+3] == player and f[i+6] == player and f[i] == str(i+1):
            return i
    #Check open diagonal top left bottom rechts top
    if f[4] == player and f[8] == player and f[0] == "1":
        return 0
    #Check open diagonal top left bottom rechts mitte
    elif f[0] == player and f[8] == player and f[4] == "5":
        return 4
    #Check open diagonal top left bottom rechts bottom
    elif f[0] == player and f[4] == player and f[8] == "9":
        return 8
    #Check open diagonal bottom left top rechts top
    elif f[4] == player and f[6] == player and f[2] == "3":
        return 2
    #Check open diagonal bottom left top rechts mitte
    elif f[2] == player and f[6] == player and f[4] == "5":
        return 4
    #Check open diagonal bottom left top rechts bottom
    elif f[2] == player and f[4] == player and f[6] == "7":
        return 6

def check_finish(f):
    finished = False
    #fields horizontal
    for i in range(3):
        if f[i*3] == f[i*3+1] and f[i*3+1] == f[i*3+2]:
            print(f"Spieler {f[i*3]} hat gewonnen!")
            finished = True
        if f[i] == f[i+3] and f[i] == f[i+6]:
            print(f"Spieler {f[i]} hat gewonnen!")
            finished = True
    #fields diagonal top left bottom rechts
    if f[0] == f [4] and f[4] == f[8]:
        print(f"Spieler {f[0]} hat gewonnen!")
        finished = True
    #fields diagonal bottom left top rechts
    if f[6] == f [4] and f[4] == f[2]:
        print(f"Spieler {f[6]} hat gewonnen!")
        finished = True
    return finished

def main():
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
    fields = ["1","2","3","4","5","6","7","8","9"]
    player = "X"
    print_fields(fields)
    end = False
    while end == False:
        if computerplay == False:
            print(f"Spieler {player} ist dran!")
            spielzug = input("Bitte ein Feld eingeben: ")
            while True:
                    if spielzug in fields and spielzug != "X" and spielzug != "0":
                        print("Spielzug: ", spielzug)
                        break
                    else:
                        print("Gebe eine gültige Zahl ein!")
                        spielzug = input("Bitte ein Feld eingeben: ")
            fields[int(spielzug)-1] = player
            if player == "X":
                player = "0"
            else:
                player = "X"
            print_fields(fields)
            end = True
            for i in ["1","2","3","4","5","6","7","8","9"]:
                if i in fields:
                    end = False
            if end == True:
                print("Unentschieden")
                break
            end = check_finish(fields)
        else:
            if player == "X":
                print("Du (X) bist dran!")
                spielzug = input("Bitte ein Feld eingeben: ")
                while True:
                        if spielzug in fields and spielzug != "X" and spielzug != "0":
                            print("Spielzug: ", spielzug)
                            break
                        else:
                            print("Gebe eine gültige Zahl ein!")
                            spielzug = input("Bitte ein Feld eingeben: ")
                fields[int(spielzug)-1] = player
                print_fields(fields)
                end = True
                for i in ["1","2","3","4","5","6","7","8","9"]:
                    if i in fields:
                        end = False
                if end == True:
                    print("Unentschieden")
                    break
                player = "0"
            else:
                print("Der Computer (0) ist dran!")
                if "0" not in fields:
                    if fields[4] == "5":
                        fields[4] = "0"
                        print("Spielzug des Computers: 5")
                    else:
                        random_corner = get_random_corner(fields)
                        fields[random_corner] = "0"
                        print("Spielzug des Computers:", random_corner + 1)
                elif fields[0] == "X" and fields[8] == "X" and fields.count("0") == 1 or fields[2] == "X" and fields[6] == "X" and fields.count("0") == 1:
                    random_kante = get_random_side(fields)
                    fields[random_kante] = "0"
                    print("Spielzug des Computers:", random_kante + 1)
                elif check_close("0", fields) != None:
                    print("Spielzug des Computers:", check_close("0", fields) + 1)
                    fields[check_close("0", fields)] = "0"
                elif check_close("X", fields) != None:
                    print("Spielzug des Computers:", check_close("X", fields) + 1)
                    fields[check_close("X", fields)] = "0"
                else:
                    try:
                        random_corner = get_random_corner(fields)
                        fields[random_corner] = "0"
                        print("Spielzug des Computers:", random_corner + 1)
                    except:
                        random_side = get_random_side(fields)
                        fields[random_side] = "0"
                        print("Spielzug des Computers:", random_side + 1)
                print_fields(fields)
                end = check_finish(fields)
                player = "X"
print("TicTacToe - Das Spiel")
print("-----------------------------\n")
end = False
while end == False:
    main()
    while True: #New Round Query
        new_round = input("Möchtest du weiterspielen? [y/n]")
        if new_round == "y":
            end = False
            break
        elif new_round == "n":
            print("TicTacToe wird beendet ", end = "", flush= True)
            for i in range(3):
                sleep(0.7)
                print(".", end = "", flush=True)
            end = True
            sleep(3)
            print("\nTicTacToe beendet!")
            break
        else:
            print("Gebe eine richtige Antwort an!")