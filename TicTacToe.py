cases = [1,2,3,4,5,6,7,8,9] #initialiser ma grille de neuf cases

def affichage(): #fonction pour afficher ma grille
        for i in range(0, len(cases), 3): #boucle pour afficher le contenu de ma grille sur trois ligne et d'avancer par trois cases
            print(f"{cases[i]}|{cases[i+1]}|{cases[i+2]}")
affichage()
    #|1|2|3|
    #|4|5|6|
    #|7|8|9|

#choix d'une case par les joueurs a tour de role
choix = 0
print("choisissez une case entre 1 et 9")
choix = int(input("joueur X : "))
cases[choix-1]="X"
affichage()
print("choisissez une case entre 1 et 9")
choix = int(input("joueur X : "))
cases[choix-1]="O"
affichage()

#conditions necessaire :
#ne peut choisir qu'un chiffre entre 1 et 9
#ne peut choisir un chiffre déja choisi
#input ne peut etre qu'un integer 
#si allignement fin partie 
#si plus de cases disponible fin partie
#boucle tant qu'un condition n'est pas remplie