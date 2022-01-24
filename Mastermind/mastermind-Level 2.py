###### Program writen by Michon Antonin
###### 20/01/2022  === Python 3.10.0 === 64bit
######====MasterMind=====###### {v1.9.7}
from random import randint


# Color Dict :

color_library = {'blanc':1, 'jaune':2, 'rouge':3, 'bleu':4, 'vert':5, 'noir':6, 'violet':7, 'marron':8 }


def clean():
    """[Nettoie l'affichage console en sautant 50 lignes]
    """
    for a in range(50):
        print("\n")



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
            user = input("Entrer la première lettre votre couleur {} en toute lettre : ==>".format(a+1)).lower()
            if user in tab :
                is_color = True
            else : 
                print("Vous n'avez pas rentrer un couleur, ou celle ci est mal orthographiée ou indisponible.")
        letter.append(user)
    liste = []
    for b in range(5):
        liste.append(color_library[letter[b]])
    return liste


##############################
# Variables :

color = ["blanc", "jaune", "rouge", "bleu", "vert", "noir", "violet", "marron"]
color_code = color_choice()
user_code = user(color)
running = True
error_left = 10
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
            print("La case {} est juste".format(a+1))
            verification +=1
            right = True
        for b in range(5) :
            if usr[b] == pc[a] :
                color = True
        if color and not right :
            print("La couleur de la case {} est correct mais pas au bon emplacement".format(a+1))
        if not color and not right :
            print("La couleur de la case {} n'est pas présente dans la combinaison.".format(a+1))


def verif():
    """[Vérifie si les 2 compositions sont les mêmes]

    Returns:
        [bool]: [True si combinaison joueur == ordinateur]
    """
    global verification
    global running
    if verification == 5 :
        print("Vous avez trouvé la combinaison, félicitation !")
        return True
    else :
        print("La combinaison n'est pas correct, il vous reste encore {} essais...".format(error_left-1))
        return False

while running :
    clean()
    comparaison(color_code, user_code)
    if verif():
        running = False
    else :
        user(color)