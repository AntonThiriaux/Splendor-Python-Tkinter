from tkinter import *
from Images.create_images import *

from game import Game
from player import Player

quit_button_image = createSingleImage('erase_image', 35, 35)


def numberOfPlayers(root):
  root.geometry('720x405')
  root.overrideredirect(True)
  
  lbInfoBackground = Label(root, bg='#0557a2', width=720, height=405)
  lbInfoBackground.place(x=-1, y=-1)
  
  global tabEntry
  tabEntry = ['enPlayer1', 'enPlayer2', 'enPlayer3', 'enPlayer4', 'lbPlayer1', 'lbPlayer2', 'lbPlayer3', 'lbPlayer4']
  global entryDict, labelDict
  entryDict = {}
  labelDict = {}

  def startGame(tab):
    gameRoot = Toplevel() #racine de la fenetre du jeu
    newGame = Game(gameRoot) #nom de la partie
    playerDict = {} #dictionnaires de joueurs
    for i in range(1, len(tab)+1):
      playerDict[f'player_{i}'] = Player(gameRoot, tab[i-1], i) #creation des joueurs: parametres sont (racine de la fenetre, nom et numero)
    newGame.launch(playerDict)
    root.destroy()


  def verifyEntries(e):
    print('here')
    lbErrorMess.config(text='')
    tab = []
    print(entryDict.keys())
    for elt in entryDict.keys():
      tab.append(entryDict[elt].get())
    for elt in tab:
      if elt == '' or elt == ' '*len(elt):
        lbErrorMess.config(text="⚠ Merci d'entrer un nom complet pour chacun des partcipants.")
        return
    startGame(tab)
    
  

  lbNumPlayers = Label(root, text="Selectionnez le nombre de joueurs: ", font=('Roboto', 14), bg='#0557a2', fg='#EEEEEE')
  lbNumPlayers.place(x=40, y=48)
  
  def showEntryPlayers(variable):
    lbErrorMess.config(text='')
    for elt in entryDict.keys():
      entryDict[elt].destroy()
    for elt in labelDict.keys():
      labelDict[elt].destroy()
    cpt = variable
    for i in range(cpt):
      entryDict[tabEntry[i]] = Entry(root, width=15)
      entryDict[tabEntry[i]].config(font=('Times New Roman', 17))
      entryDict[tabEntry[i]].config(relief=FLAT)
      labelDict[tabEntry[i+4]] = Label(root, text=f'Nom du joueur #{i+1}:', font=('Times New Roman', 12), bg='#0557a2', fg='#EEEEEE')
    for i in range(2):
      for j in range(2):
        if cpt > 0:
          if i == 0:
            entryDict[f'enPlayer{i+j+1}'].place(x=100+j*300, y=186)
            labelDict[f'lbPlayer{i+j+1}'].place(x=100+j*300, y=162)
          else:
            entryDict[f'enPlayer{i+j+2}'].place(x=100+j*300, y=266)
            labelDict[f'lbPlayer{i+j+2}'].place(x=100+j*300, y=242)
          cpt -= 1
          

  optionNumberPlayers = [2, 3, 4]
  
  variable = StringVar(root)
  variable.set(optionNumberPlayers[0])# default value
  lbEnterNames = Label(root, text="Saisissez le nom de chaque participant dans les cases ci-dessous.", font=('Roboto', 12), bg='#0557a2', fg='#EEEEEE')
  lbEnterNames.place(x=360, y=110, anchor=N)
  numPlayers = OptionMenu(root, variable, *optionNumberPlayers, command=showEntryPlayers)
  numPlayers.config(bg='#0557a2', fg='#EEEEEE', activebackground='#0557a2', activeforeground='#EEEEEE', relief=FLAT, font=('Roboto', 14))
  numPlayers['menu'].config(bg='#EEEEEE', fg='#0557a2', relief=FLAT, activebackground='#0557a2', activeforeground='#EEEEEE', font=('Lucida Sans Typewriter', 11))
  numPlayers.place(x=382, y=42)

  global lbErrorMess
  lbErrorMess = Label(root, text='', fg='#DE6060', bg='#0557a2', font=('Arial', 11, 'bold'))
  lbErrorMess.place(x=360, y=343, anchor=S)

  btConfirmInscription = Button(root, text='Valider', font=('Roboto', 12), relief=FLAT, bg='#0557a2', activebackground='#EEEEEE', fg='#EEEEEE', activeforeground='#0557a2')
  btConfirmInscription.place(x=360, y=385, anchor=S)

  showEntryPlayers(2)

  btReturnToMenu = Button(root, image=quit_button_image, bg='#0557a2', activebackground='#0557a2', highlightbackground='#0557a2', relief=FLAT, command=lambda: root.destroy())
  btReturnToMenu.place(x=710, y=10, anchor=NE)


  
  btConfirmInscription.bind('<Button-1>', verifyEntries)
  root.bind('<Return>', verifyEntries)