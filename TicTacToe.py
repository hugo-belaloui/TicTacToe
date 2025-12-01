cases = [1,2,3,4,5,6,7,8,9] #initialiser ma grille de neuf cases

def affichage(): #fonction pour afficher ma grille
        for i in range(0, len(cases), 3): #boucle pour afficher le contenu de ma grille sur toi ligne et d'avancer par trois 
            print(f"{cases[i]}|{cases[i+1]}|{cases[i+2]}")
            if i == 6:
                break
affichage()




    #|1|2|3|
    #|4|5|6|
    #|7|8|9|
