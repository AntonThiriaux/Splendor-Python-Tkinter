from tkinter import *
from Images.create_images import *


from bank import Bank
global image
image = createSingleImage('board_background', 570, 345)


class Board:
  def __init__(self, root):
    self.frame = Frame(root, width=570, height=345)
    self.frame.place(x=0, y=0)
    lbBoardBackground = Label(self.frame, image=image)
    lbBoardBackground.place(x=-1, y=-1)
    self.list_stack_1 = []
    self.list_stack_2 = []
    self.list_stack_3 = []
    self.list_nobles = []

  def displayBoard(self, func):
    for i in range(len(self.list_stack_3)):
      frStack3 = Frame(self.frame, width=58, height=83)
      frStack3.place(x=126+i*67, y=13)
      image = createImageInList(self.list_stack_3[i], 3)
      btTest = Button(frStack3, image=image, command=lambda i=i: func(3, self.list_stack_3[i]))
      btTest.image = image
      btTest.place(x=-7, y=-2)
    for i in range(len(self.list_stack_2)):
      frStack2 = Frame(self.frame, width=58, height=83)
      frStack2.place(x=126+i*67, y=104)
    for i in range(len(self.list_stack_1)):
      frStack1 = Frame(self.frame, width=58, height=83)
      frStack1.place(x=126+i*67, y=196)
    #display list_nobles

  def place_cards(self, bank, nb_players):
    for i in range(0, 4):
      self.list_stack_1.append(bank.stack_cards_1.unstack())
      self.list_stack_2.append(bank.stack_cards_2.unstack())
      self.list_stack_3.append(bank.stack_cards_3.unstack())
    for i in range(nb_players + 1):
      self.list_nobles.append(bank.stack_nobles.unstack())

  def affichage_liste(self, list): 
    content = ''
    for i in range(len(list)):
      content = content + ' | ' + list[i]
    content = content + ' | '
    return content

  def affichage_dict(self, dict):
    content = ''
    for elt in dict.keys():
      content = content + ' | ' + elt + ': ' + str(dict[elt])
    content = content + ' | '
    return content
  
  def affiche(self, bank):
    print('='*120)
    print('Board')
    print('|| Nobles :   ', self.affichage_liste(self.list_nobles))
    print('||','-'*117)
    print('|| Cards 3:   ', self.affichage_liste(self.list_stack_3))
    print('|| Cards 2:   ', self.affichage_liste(self.list_stack_2))
    print('|| Cards 1:   ', self.affichage_liste(self.list_stack_1))
    print('||', '-'*117,)
    print('|| Tokens :   ', self.affichage_dict(bank.list_token))
    print("="*120)