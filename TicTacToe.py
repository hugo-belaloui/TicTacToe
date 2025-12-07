import random

grid = [1,2,3, #initialiser ma grille "vide" de neuf cases
        4,5,6,
        7,8,9] 

winning_cases = [[0,1,2], (3,4,5), (6,7,8), (0,3,6), #initialiser liste de listes de victoire possible
                (1,4,7), (2,5,8), (0,4,8), (2,4,6)]  #important de commencer par l'index zero

choice = 0 
choice_player = 0
player_count = 1
game_on_off = True
difficulty_choice = 0

def average_difficulty_choice_ai(): # difficultés normal
    for i in winning_cases: #parcourt les elements des possibilitées de gain
        j_tab = [] #crée une liste vide 
        for j in i: #parcourt les elements de la liste
            j_tab.append(grid[j])
        n_tab = sum(1 for k in j_tab if isinstance(k, str)) #parcourt la liste et somme les 'char' est entier
        if n_tab == 2 :
            n_tab_x = j_tab.count('X')
            n_tab_o = j_tab.count('O')
            if n_tab_o == 2 : #si les deux cases prises gagne
                for i_grid in i:
                    if isinstance(grid[i_grid], int):
                        grid[i_grid]='X'
                        return
            elif n_tab_x == 2: #si les deux cases prises empeche de gagner
                for i_grid in i:
                    if isinstance(grid[i_grid], int):
                        grid[i_grid]='O'
                        return
            elif isinstance(grid[4], int): #sinon si le centre est vide (forte probas de gagner)
                grid[4]='O'
                return
            else:
                grid[random.choice([i for i, x in enumerate(grid) if isinstance(x, int)])] = 'O'
                return

def random_choice_ai (): #fonction dont l'output est uniquement un integer choisi depuis la list grid
    return random.choice([i for i, x in enumerate(grid) if isinstance(x, int)]) #parcourir tout les elements de grid et creer une liste contenant tout intergers en récuperant l'index et la valeur associé 

def display(): #fonction pour afficher ma grille
        for i in range(0, len(grid), 3): #boucle pour afficher le contenu de ma grille sur trois ligne et d'avancer par trois cases
            print(f"{grid[i]}|{grid[i+1]}|{grid[i+2]}")
    #display()
    #|1|2|3|
    #|4|5|6|
    #|7|8|9|

def input_choice(player): #boucle pour gérer les conditions d'input et les erreurs
    while True: 
            if game_mode == 1:
                try : 
                    print("Choisissez une case entre 1 et 9")
                    if player % 2 == 0 :
                        n_choice = int(input("joueur X :\n> "))
                    else :
                        n_choice = int(input("joueur O :\n> "))
                    if  1 <= n_choice <= 9 : #verifie la plage
                        if isinstance(grid[n_choice-1], int): #verifie qu'il s'agit d'un int
                            return n_choice-1
                        else : 
                            print("case déja prise, réessayez")
                    else :
                        print("Erreur, le chiffre doit etre entre 1 et 9")
                except ValueError: #il ne s'agit pas d'un int
                    print("Erreur, la valeur ne peut pas etre un string et doit etre un chiffre entre 1 et 9")
            else :
                # if play mode == 2 :
                    try : 
                        print("Choisissez une case entre 1 et 9")
                        n_choice = int(input("joueur X :\n> "))
                        if  1 <= n_choice <= 9 : #verifie la plage
                            if isinstance(grid[n_choice-1], int): #verifie qu'il s'agit d'un int
                                return n_choice-1
                            else : 
                                print("case déja prise, réessayez")
                        else :
                            print("Erreur, le chiffre doit etre entre 1 et 9")
                    except ValueError: #il ne s'agit pas d'un int
                        print("Erreur, la valeur ne peut pas etre un string et doit etre un chiffre entre 1 et 9")
                # else :
                #     n_choice = random_choice_ai()
                #     return n_choice

def check_victory(input_grid_function): #fonction pour verifier les conditions de victoire
    for i,j,k in winning_cases:
        if input_grid_function[i] == input_grid_function[j] == input_grid_function[k]: # verifie les 8 scenario de victoire
            if player_count % 2 == 0 :
                print("victoire joueur X")
                return True
            else : 
                print("victoire joueur O")
                return True
    if not any(isinstance(i, int) for i in input_grid_function): #verifie si il n'y a plus de case 'integers' vide
            print("match nul")  
            return True

print("pour jouer contre un autre joueur tappez '1' \npour jouer contre un robot tappez '2'")

while True:#choix du mode de jeu avec gestion des exceptions d'input
    try :
        game_mode = int(input("> "))
        if game_mode in [1, 2]:
            break
        else :
            print("la valeur doit etre 1 ou 2")
    except ValueError:
        print("Erreur, la valeur ne peut pas etre un string et doit etre soit 1 soit 2")

if game_mode == 2: #input choix difficulté
    print("choissisez une difficulté \n 1 pour facile \n 2 pour normal")
    while True:
        try :
            difficulty_choice = int(input("> "))
            if difficulty_choice in [1, 2]:
                break
            else :
                print("la valeur doit etre 1 ou 2")
        except ValueError:
            print("Erreur, la valeur ne peut pas etre un string et doit etre soit 1 soit 2")


while game_on_off: #boucle de jeu
    if game_mode == 1: 
        if player_count % 2 == 0 : #condition tour joueur 
            print("tour du joueur X")
            grid[input_choice(player_count)] = 'X' #input le symbole correspondant dans la grid 
            display() 
            if check_victory(grid): # appelle la fonction de verification de victoire
                game_on_off = False 
        else :
            print("tour du joueur O")
            grid[input_choice(player_count)] = 'O'
            display()
            if check_victory(grid):
                game_on_off = False
    else :  #game mode 2
        if difficulty_choice == 1 : #difficulté facile
            if player_count % 2 == 0 :
                print("Votre tour X")
                grid[input_choice(player_count)] = 'X' 
                display() 
                if check_victory(grid): 
                    game_on_off = False 
            else :
                print("tour du robot O")
                grid[random_choice_ai()] = 'O'
                display()
                if check_victory(grid):
                    game_on_off = False
        if difficulty_choice == 2 : #difficulté difficile
            if player_count % 2 == 0 :
                print("Votre tour X")
                grid[input_choice(player_count)] = 'X' 
                display() 
                if check_victory(grid): 
                    game_on_off = False 
            else :
                print("tour du robot O")
                average_difficulty_choice_ai()
                display()
                if check_victory(grid):
                    game_on_off = False
    player_count+=1




# choice = input_choice()
# grid[choice] = 'X'
# display()

#conditions necessaire :
#ne peut choisir qu'un chiffre entre 1 et 9
#ne peut choisir un chiffre déja choisi
#input ne peut etre qu'un integer, renvoie une erreur 
#si allignement fin partie 
#si plus de cases disponible fin partie
#boucle tant qu'un condition n'est pas remplie
