grid = [1,2,3, #initialiser ma grille "vide" de neuf cases
        4,5,6,
        7,8,9] 

winning_cases = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), #initialiser liste de listes de victoire possible
                (1,4,7), (2,5,8), (0,4,8), (2,4,6)]  #important de commencer par l'index zero
choice = 0 
player_count = 1
game_on_off = True 


def display(): #fonction pour afficher ma grille
        for i in range(0, len(grid), 3): #boucle pour afficher le contenu de ma grille sur trois ligne et d'avancer par trois cases
            print(f"{grid[i]}|{grid[i+1]}|{grid[i+2]}")
    #display()
    #|1|2|3|
    #|4|5|6|
    #|7|8|9|

def input_choice(player): #boucle pour gérer les conditions d'input et les erreurs
    while True: 
            try : 
                print("Choisissez une case entre 1 et 9")
                if player % 2 == 0 :
                    n_choice = int(input("joueur X : "))
                else :
                    n_choice = int(input("joueur O : "))
                if  1 <= n_choice <= 9 : #verifie la plage
                    if isinstance(grid[n_choice-1], int): #verifie qu'il s'agit d'un int
                        return n_choice-1
                    else : 
                        print("case déja prise, réessayez")
                else :
                    print("Erreur, le chiffre doit etre entre 1 et 9")
            except ValueError: #il ne s'agit pas d'un int
                print("Erreur, la valeur ne peut pas etre un string et doit etre un chiffre entre 1 et 9")

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




while game_on_off: #boucle de jeu
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
