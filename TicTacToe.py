from time import sleep
import random
global fields

def print_fields():
    for i in range(3):
        print(fields[i*3] + " | " + fields[i*3+1] + " | " + fields[i*3+2] )

def get_random_corner():
    corners = []
    for i in [0,2,6,8]:
        if fields[i] == str(i+1):
            corners.append(i)
    return random.choice(corners)

def get_random_side():
    sides = []
    for i in [1,3,5,7]:
        if fields[i] == str(i+1):
            sides.append(i)
    return random.choice(sides)

def check_close(player):
    for i in range(3):
        #Check open horizontal left
        if fields[i*3+1] == player and fields[i*3+2] == player and fields[i*3] == str(i*3+1):
            return i*3
        #Check open horizontal mitte
        elif fields[i*3] == player and fields[i*3+2] == player and fields[i*3+1] == str(i*3+2):
            return i*3+1
        #Check open horizontal rechts
        elif fields[i*3] == player and fields[i*3+1] == player and fields[i*3+2] == str(i*3+3):
            return i*3+2    
        #Check open vertical bottom
        elif fields[i] == player and fields[i+3] == player and fields[i+6] == str(i+7):
            return i+6
        #Check open vertical mitte
        elif fields[i] == player and fields[i+6] == player and fields[i+3] == str(i+4):
            return i+3
        #Check open vertical top
        elif fields[i+3] == player and fields[i+6] == player and fields[i] == str(i+1):
            return i
    #Check open diagonal top left bottom rechts top
    if fields[4] == player and fields[8] == player and fields[0] == "1":
        return 0
    #Check open diagonal top left bottom rechts mitte
    elif fields[0] == player and fields[8] == player and fields[4] == "5":
        return 4
    #Check open diagonal top left bottom rechts bottom
    elif fields[0] == player and fields[4] == player and fields[8] == "9":
        return 8
    #Check open diagonal bottom left top rechts top
    elif fields[4] == player and fields[6] == player and fields[2] == "3":
        return 2
    #Check open diagonal bottom left top rechts mitte
    elif fields[2] == player and fields[6] == player and fields[4] == "5":
        return 4
    #Check open diagonal bottom left top rechts bottom
    elif fields[2] == player and fields[4] == player and fields[6] == "7":
        return 6

def check_finish():
    finished = False
    global fields
    #fields horizontal
    for i in range(3):
        if fields[i*3] == fields[i*3+1] and fields[i*3+1] == fields[i*3+2]:
            print(f"Spieler {fields[i*3]} hat gewonnen!")
            finished = True
        if fields[i] == fields[i+3] and fields[i] == fields[i+6]:
            print(f"Spieler {fields[i]} hat gewonnen!")
            finished = True
    #fields diagonal top left bottom rechts
    if fields[0] == fields [4] and fields[4] == fields[8]:
        print(f"Spieler {fields[0]} hat gewonnen!")
        finished = True
    #fields diagonal bottom left top rechts
    if fields[6] == fields [4] and fields[4] == fields[2]:
        print(f"Spieler {fields[6]} hat gewonnen!")
        finished = True
    return finished

def main():
    global fields
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
    print_fields()
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
            print_fields()
            end = True
            for i in ["1","2","3","4","5","6","7","8","9"]:
                if i in fields:
                    end = False
            if end == True:
                print("Unentschieden")
                break
            end = check_finish()
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
                print_fields()
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
                        random_corner = get_random_corner()
                        fields[random_corner] = "0"
                        print("Spielzug des Computers:", random_corner + 1)
                elif fields[0] == "X" and fields[8] == "X" and fields.count("0") == 1 or fields[2] == "X" and fields[6] == "X" and fields.count("0") == 1:
                    random_kante = get_random_side()
                    fields[random_kante] = "0"
                    print("Spielzug des Computers:", random_kante + 1)
                elif check_close("0") != None:
                    print("Spielzug des Computers:", check_close("0") + 1)
                    fields[check_close("0")] = "0"
                elif check_close("X") != None:
                    print("Spielzug des Computers:", check_close("X") + 1)
                    fields[check_close("X")] = "0"
                else:
                    try:
                        random_corner = get_random_corner()
                        fields[random_corner] = "0"
                        print("Spielzug des Computers:", random_corner + 1)
                    except:
                        random_side = get_random_side()
                        fields[random_side] = "0"
                        print("Spielzug des Computers:", random_side + 1)
                print_fields()
                end = check_finish()
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
            print("TicTacToe wird beendt ", end = "", flush= True)
            for i in range(3):
                sleep(0.7)
                print(".", end = "", flush=True)
            end = True
            sleep(3)
            print("\nTicTacToe beendet!")
            break
        else:
            print("Gebe eine richtige Antwort an!")