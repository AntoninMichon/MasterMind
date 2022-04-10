from niveau1 import level1
from niveau2 import level2
from niveau3 import level3

def mastermind():
    print("Bonjour et bienvenu sur ce Jeu du mastermind uniquement en console")
    print("Il y a trois niveaux de difficulté, pour en savoir plus, lisez le fichier README.md")
    print("Si vous souhaitez arreter le programme, lors de n'importe quelle saisi, tapez stop")
    def selection ():
        liste = [1, 2, 3]
        right = False
        while not right :
            user = input("Choisissez votre niveau (1, 2 ou 3) => ")
            if user == "stop" :
                exit()
            if int(user) in liste :
                right = True
            else :
                print("Votre séléction du niveau n'est pas correct. Veulliez réessayer.")
                
        return int(user)
    
    def launch(nbr):
        if nbr == 1:
            level1()
        if nbr == 2:
            level2()
        if nbr == 3:
            level3()
    
    while True :
        launch(selection())
        
mastermind()