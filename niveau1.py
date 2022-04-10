###### Program writen by Michon Antonin
#?##### 20/01/2022  === Python 3.9.7 === 64bit
#?#####====MasterMind=====###### {v2.1.3}

def level1():
    # !Imports :
    from random import randint


    # !Script
    def computer(tab) :
        
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
            nbr = randint(0, len(tab)-1)
            if tab[nbr] not in liste and not full :
                liste.append(tab[nbr])
        return liste 


    def user(tab, verif) :
        
        """Demande a l'utilisateur de rentrer sa combinaison

        Args:
            tab (list): Couleur Disponible
            verif (list): Vérifie si on ne redemande pas une couleur juste

        Returns:
            list: liste de l'utilisateur
        """
        
        liste = [None, None, None, None, None]
        
        for i in range(5):
            if not verif[i] :
                right = False
                while not right :
                    user = input("\nEntrer la couleur {} => ".format(i+1)).lower()
                    if user == "stop" :
                        exit()
                    if user in tab :
                        right = True
                    else :
                        print("Vous n'avez pas rentrer un couleur, ou celle ci est mal orthographiée ou indisponible.")
                    liste[i] = user
                    
        return liste
            
            
    #?##########################
    # !Variables :

    #?=========PRÉFÉRENCE========#
    color = ["blanc", "jaune", "rouge", "bleu", "vert", "noir", "violet", "marron"]     #* Si vous le souhaitez, vous pouvez rajouter une couleur ici.
    error = input("Entrer le nombre d'erreur maximum que vous souhaitez\n=>")
    if error == "stop" :
        exit()
    error_left = int(error)
    #?===========================#

    verification = 0
    running = True
    entrer =[False, False, False, False, False]
    ordi_combi = computer(color)
    user_combi = user(color, entrer)
    #?#########################

    def comparaison(pc, usr) :
        
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
        for a in range(5) :
            right = False
            color = False
            if pc[a] == usr[a] :
                print("\nLa case {} est juste".format(a+1))
                verification +=1
                right = True
                entrer[a] = True
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
            print("Vous avez trouvé la combinaison, félicitation !")
            return True
        if nbr == 1 :
            print("\n\nRéponse :\n")
            for i in range(5) :
                print("La couleur {} était le  {}.\n".format(i+1, tab[i]))
            return True
        else :
            error_left -= 1
            print("\nLa combinaison n'est pas correct, il vous reste encore {} essais...".format(error_left))
            return False

    # !Boucle :
    while running :
        
        """Boucle final
        """
        
        comparaison(ordi_combi, user_combi)
        
        if verif(error_left, ordi_combi):
            running = False
        else :
            user(color, entrer)