from time import sleep
import random
import gettext
import locale

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
    winner = None
    #fields horizontal
    for i in range(3):
        if f[i*3] == f[i*3+1] and f[i*3+1] == f[i*3+2]:
            winner = f[i*3]
        if f[i] == f[i+3] and f[i] == f[i+6]:
            winner = f[i]
    #fields diagonal top left bottom rechts
    if f[0] == f [4] and f[4] == f[8]:
        winner = f[0]
    #fields diagonal bottom left top rechts
    if f[6] == f [4] and f[4] == f[2]:
        winner = f[6]
    if winner != None:
        formatted_text = _("Spieler {winner} hat gewonnen!").format(winner = winner)
        print(formatted_text)
        finished = True
    return finished

def main():
    computerplay = False
    while True:
        print(_("Möchtest du gegen den Computer [c] oder gegen einen Menschen [m] spielen? "), end = "")
        mode = input()
        if mode == "c":
            computerplay = True
            break
        elif mode == "m":
            computerplay = False
            break
        else:
            print(_("Gebe eine richtige Antwort ein!"))
    fields = ["1","2","3","4","5","6","7","8","9"]
    player = "X"
    print_fields(fields)
    end = False
    while end == False:
        if computerplay == False:
            formatted_text = _("Spieler {player} ist dran!").format(player = player)
            print(formatted_text)
            print(_("Bitte ein Feld eingeben: "), end = "")
            move = input()
            while True:
                    if move in fields and move != "X" and move != "0":
                        formatted_text = _("Spielzug: {move}").format(move=move)
                        print(formatted_text)
                        break
                    else:
                        print(_("Gebe ein gültiges Feld ein!"))
                        print(_("Bitte ein Feld eingeben: "), end = "")
                        move = input()
            fields[int(move)-1] = player
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
                print(_("Unentschieden"))
                break
            end = check_finish(fields)
        else:
            if player == "X":
                formatted_text = _("Spieler {player} ist dran!").format(player = player)
                print(formatted_text)
                print(_("Bitte ein Feld eingeben: "), end = "")
                move = input()
                while True:
                    if move in fields and move != "X" and move != "0":
                        formatted_text = _("Spielzug: {move}").format(move=move)
                        print(formatted_text)
                        break
                    else:
                        print(_("Gebe ein gültiges Feld ein!"))
                        print(_("Bitte ein Feld eingeben: "), end = "")
                        move = input()
                fields[int(move)-1] = player
                print_fields(fields)
                end = True
                for i in ["1","2","3","4","5","6","7","8","9"]:
                    if i in fields:
                        end = False
                if end == True:
                    print(_("Unentschieden"))
                    break
                player = "0"
            else:
                print(_("Der Computer (0) ist dran!"))
                if "0" not in fields:
                    if fields[4] == "5":
                        fields[4] = "0"
                        print(_("Spielzug des Computers: 5"))
                    else:
                        random_corner = get_random_corner(fields)
                        fields[random_corner] = "0"
                        formatted_text = _("Spielzug des Computers: {field}").format(field = random_corner + 1)
                        print(formatted_text)
                elif fields[0] == "X" and fields[8] == "X" and fields.count("0") == 1 or fields[2] == "X" and fields[6] == "X" and fields.count("0") == 1:
                    random_side = get_random_side(fields)
                    fields[random_side] = "0"
                    formatted_text = _("Spielzug des Computers: {field}").format(field = random_side + 1)
                    print(formatted_text)
                elif check_close("0", fields) != None:
                    formatted_text = _("Spielzug des Computers: {field}").format(field = check_close("0", fields) + 1)
                    print(formatted_text)
                    fields[check_close("0", fields)] = "0"
                elif check_close("X", fields) != None:
                    formatted_text = _("Spielzug des Computers: {field}").format(field = check_close("X", fields) + 1)
                    print(formatted_text)
                    fields[check_close("X", fields)] = "0"
                else:
                    try:
                        random_corner = get_random_corner(fields)
                        fields[random_corner] = "0"
                        formatted_text = _("Spielzug des Computers: {field}").format(field = random_corner + 1)
                        print(formatted_text)
                    except:
                        random_side = get_random_side(fields)
                        fields[random_side] = "0"
                        formatted_text = _("Spielzug des Computers: {field}").format(field = random_side + 1)
                        print(formatted_text)
                print_fields(fields)
                end = check_finish(fields)
                player = "X"

#Initialise multilanguage support
system_language, _ = locale.getlocale()
if system_language.startswith('de'):
    _ = gettext.gettext
else:
    en = gettext.translation('base', localedir='locales', languages=['en'])
    en.install()
    _ = en.gettext

#Start Game
print(_("TicTacToe - Das Spiel"))
print("-----------------------------\n")
end = False
while end == False:
    main()
    while True: #New Round Query
        print(_("Möchtest du weiterspielen? [y/n] "), end = "")
        new_round = input()
        if new_round == "y":
            end = False
            break
        elif new_round == "n":
            print(_("TicTacToe wird beendet "), end = "", flush= True)
            for i in range(3):
                sleep(0.7)
                print(".", end = "", flush=True)
            end = True
            sleep(3)
            print(_("\nTicTacToe beendet!"))
            break
        else:
            print(_("Gebe eine richtige Antwort an!"))