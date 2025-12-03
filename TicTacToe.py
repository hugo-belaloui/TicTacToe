cases = [1,2,3,
        4,5,6,
        7,8,9] #initialiser ma grille de neuf cases

def affichage(): #fonction pour afficher ma grille
        for i in range(0, len(cases), 3): #boucle pour afficher le contenu de ma grille sur trois ligne et d'avancer par trois cases
            print(f"{cases[i]}|{cases[i+1]}|{cases[i+2]}")
affichage()
    #|1|2|3|
    #|4|5|6|
    #|7|8|9|

#choix d'une case par les joueurs a tour de role
choix = 0
def entree_choix(): #boucle pour gérer les conditions d'input et les erreurs
    while True: 
            print("Choisissez une case entre 1 et 9")
            n_choix = int(input("joueur X : ")) 
            if  1 <= n_choix <= 9 : #verifie la plage
                if isinstance(cases[n_choix-1], int): #verifie qu'il s'agit d'un int
                    return n_choix
                else : 
                    print("case déja prise, réessayez")
            elif ValueError: #il ne s'agit pas d'un int
                print("Erreur, la valeur ne peut pas etre un string et doit etre un chiffre entre 1 et 9")
            else :
                print("Erreur, le chiffre doit etre entre 1 et 9")

choix = entree_choix()

#conditions necessaire :
#ne peut choisir qu'un chiffre entre 1 et 9
#ne peut choisir un chiffre déja choisi
#input ne peut etre qu'un integer, renvoie une erreur 
#si allignement fin partie 
#si plus de cases disponible fin partie
#boucle tant qu'un condition n'est pas remplie