###### Program writen by Michon Antonin
###### 20/01/2022  === Python 3.10.0 === 64bit
######====MasterMind=====###### {v1.9.7}

# Import :
from random import randint


# Color Dict :
color_library = {'blanc':1, 'jaune':2, 'rouge':3, 'bleu':4, 'vert':5, 'noir':6, 'violet':7, 'marron':8 }

# Script :
def color_choice():
    
    """[Génère une composition de 5 Couleurs]
    Returns:
        [list]: [Composition ordinateur]
    """
    liste = []
    for a in range(5):
        nbr = randint(1, 8)
        liste.append(nbr)
    return liste


# Script
def user(tab):
    
    """[Récupère la composition de l'utilisateur et le convertie en chiffre]

    Args:
        tab ([list]): [Couleurs acceptées]

    Returns:
        [list]: [Composition du joueur]
    """
    letter = []
    for a in range(5):
        is_color = False
        while not is_color :
            user = input("\nEntrer la première lettre votre couleur {} en toute lettre : ==>".format(a+1)).lower()
            if user in tab :
                is_color = True
            else : 
                print("\nVous n'avez pas rentrer un couleur, ou celle ci est mal orthographiée ou indisponible.")
        letter.append(user)
    liste = []
    for b in range(5):
        liste.append(color_library[letter[b]])
    return liste


##############################
# Variables :
#=========PRÉFÉRENCE========#
error_left = 8
#===========================#
color = ["blanc", "jaune", "rouge", "bleu", "vert", "noir", "violet", "marron"]
ordi_combi = color_choice()
user_combi = user(color)
running = True
verification = 0 
##############################


def comparaison(pc, usr):
    
    """[Compare la composition de l'ordinateur a celle du joueur, et renvoie
    les informations nécessaire en console]

    Args:
        pc ([list]): [combinaison ordinateur]
        usr ([list]]): [Combinaison joueur]
    """
    global error_left
    global verification
    verification = 0
    for a in range(5):
        right = False
        color = False
        if pc[a] == usr[a] :
            print("\nLa case {} est juste".format(a+1))
            verification +=1
            right = True
        for b in range(5) :
            if usr[b] == pc[a] :
                color = True
        if color and not right :
            print("\nLa couleur de la case {} est correct mais pas au bon emplacement".format(a+1))
        if not color and not right :
            print("\nLa couleur de la case {} n'est pas présente dans la combinaison.".format(a+1))


def verif(nbr, tab):
    
    """Vérifie le nombre d'erreur, si il reste des tentatives, ou si la partie est gagné.
    Args:
        nbr (int): Nombre d'erreur restante
        tab (list): Liste pour un affichage propre
        
    Returns:
        1 ) bool : Si le jeux est gagné, stop la boucle finale
        2 ) bool : Si la combinaison n'est pas correct, indique le nombre d'essaie restant
        3 ) bool : Si il n'y a plus de tentative, le jeux est perdu et la boucle stoper
    """
    
    global verification
    global running
    global error_left
    if verification == 5 :
        print("\nVous avez trouvé la combinaison, félicitation !")
        return True
    if nbr == 1 :
        print("\n\nRéponse :\n")
        for i in range(5) :
            print("\nLa couleur {} était le  {}.\n".format(i+1, tab[i]))
        return True
    else :
        error_left -= 1
        print("\nLa combinaison n'est pas correct, il vous reste encore {} essais...".format(error_left))
        return False


# Boucle Finale :
while running :
    
    comparaison(ordi_combi, user_combi)
    
    if verif(error_left, ordi_combi):
        running = False
    else :
        user(color)