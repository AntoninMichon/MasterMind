###### Program writen by Michon Antonin
###### 20/01/2022  === Python 3.10.0 === 64bit
######====MasterMind=====###### {v2.1.3}

from random import randint

def clean():
    """[Nettoie l'affichage console en sautant 50 lignes]
    """
    for a in range(50):
        print("\n")


def computer(tab):
    """Computer :
    Args:
        tab (list): liste de toute les couleur disponible

    Returns:
        list : Liste de 5 elemement string, contenant 5 couleur aléatoire
    """
    liste = []
    full = False
    while not full :
        if len(liste) == 5 :
            full = True
        nbr = randint(0, 7)
        if tab[nbr] not in liste :
            liste.append(tab[nbr])
    return liste


def user(tab, verif):
    """_summary_

    Args:
        tab (list): Couleur Disponible
        verif (list): _description_

    Returns:
        list: liste de l'utilisateur
    """
    liste = [None, None, None, None, None]
    
    if not verif[0] :
        col1 = False
        while not col1 :
            user = input("Entrer votre première couleur => ").lower()
            if user in tab :
                col1 = True
            else :
                print("Vous n'avez pas rentrer un couleur, ou celle ci est mal orthographiée ou indisponible.")
        liste[0] = user
    if not verif[1] :
        col2 = False
        while not col2 :
            user = input("Entrer votre seconde couleur => ").lower()
            if user in tab :
                col2 = True
            else :
                print("Vous n'avez pas rentrer un couleur, ou celle ci est mal orthographiée ou indisponible.")
        liste[1] = user
    if not verif[2] :
        col3 = False
        while not col3 :
            user = input("Entrer votre troisième couleur => ").lower()
            if user in tab :
                col3 = True
            else :
                print("Vous n'avez pas rentrer un couleur, ou celle ci est mal orthographiée ou indisponible.")
        liste[2] = user
    if not verif[3] :
        col4 = False
        while not col4 :
            user = input("Entrer votre quatrième couleur => ").lower()
            if user in tab :
                col4 = True
            else :
                print("Vous n'avez pas rentrer un couleur, ou celle ci est mal orthographiée ou indisponible.")
        liste[3] = user
    if not verif[4] :
        col5 = False
        while not col5 :
            user = input("Entrer votre cinquième couleur => ").lower()
            if user in tab :
                col5 = True
            else :
                print("Vous n'avez pas rentrer un couleur, ou celle ci est mal orthographiée ou indisponible.")
        liste[4] = user
        
    return liste
        
        
###########################
# Variables :
color = ["blanc", "jaune", "rouge", "bleu", "vert", "noir", "violet", "marron"]
error_left = 10
verification = 0
running = True
entrer =[False, False, False, False, False]
ordi_combi = computer(color)
print(ordi_combi)
user_combi = user(color, entrer)
##########################

def comparaison(pc, usr):
    """[Compare la composition de l'ordinateur a celle du joueur, et renvoie
    les informations nécessaire en console]

    Args:
        pc ([list]): [combinaison ordinateur]
        usr ([list]]): [Combinaison joueur]
    """
    global error_left
    global verification
    global entrer
    verification = 0
    for a in range(5):
        right = False
        color = False
        if pc[a] == usr[a] :
            print("La case {} est juste".format(a+1))
            verification +=1
            right = True
            entrer[a] = True
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
    comparaison(ordi_combi, user_combi)
    if verif():
        running = False
    else :
        user(color, entrer)