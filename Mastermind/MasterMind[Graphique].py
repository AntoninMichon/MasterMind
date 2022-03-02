##### Programme writen by Antonin Michon ;
### MasterMind Tkinter v2.1
######## THIS PROGRAM DOESN'T WORK !!!!!!!#########
from tkinter import*
from random import randint

# Fuction :
def homepage():
    # Windows create : 
    window = Tk()
    #Windows Config :
    window.title("MasterMind -- Le Jeu")
    window.geometry("1280x720")
    window.minsize(720, 480)
    window.config(background='#000000')
    # Frame :
    all = Frame(window, bg='#000000')
    right = Frame(all, bg='#000000')
    left = Frame(all, bg='#000000')
    top = Frame(all, bg='#000000')
    bottom = Frame(all, bg='#000000')
    # Text :
    label_title = Label(window, text="MasterMind -- Le Jeu\nV2.1", font=("Arial", 25), bg='#000000', fg='#FFFFFF' )
    label_title.pack(side=TOP)
    level_choice = Label(right, text="Choix du Niveau : ", font=("Arial", 20), bg='#000000', fg='#FFFFFF')
    level_choice.grid(row=0, column=0)
    level_sep = Label(right, text="=================", font=("Arial", 10), bg='#000000', fg='#FFFFFF')
    level_sep.grid(row=2, column=0)
    # Level select :
    lev1 = Button(right, text="Facile", bg='#FFFFFF', fg='#000000', command=level1)
    lev1.grid(row=1, column=0)
    lev2 = Button(right, text="Difficile", bg='#FFFFFF', fg='#000000')
    lev2.grid(row=3, column=0)

    # Program Graphic:
    all.pack(expand=YES)
    right.pack(side=RIGHT)
    left.pack(side=LEFT)
    top.pack(side=TOP)
    bottom.pack(side=BOTTOM)

    # Menu :

    menu_bar = Menu(window)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Quitter", command=window.quit)
    menu_bar.add_cascade(label="Option", menu=file_menu)


    # Screen :
    window.config(menu=menu_bar)
    window.mainloop()

def level1():
    # Windows create :
    win1 = Tk()
    # Windows config :
    win1.title("MasterMind -- Level1")
    win1.geometry("1280x720")
    win1.minsize(720, 480)
    win1.config(background='#5cb638')
    
    # Button :
    def generation():
        """[Génère une composition de 5 Couleurs]
        Returns:
            [list]: [Composition ordinateur]
        """
        
        liste = []
        complete = False
        while not complete :
            if len(liste) == 5:
                complete = True
            nbr = randint(1, 8)
            if nbr not in liste :
                liste.append(nbr)
        return liste
    
    generation()
    
    usr = Entry(win1, text="Entrer votre combinaison de couleur", bg='#FFFFFF', fg='#000000')
    usr.pack()
    def printmess():
        print(usr())
    affich = Button(win1, text="Afficher la couleur entrée", bg='#FFFFFF', fg='#000000', command=printmess)
    affich.pack()
    
    


    # Screen :
    win1.mainloop()


homepage()