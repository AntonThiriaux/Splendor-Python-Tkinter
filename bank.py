from tkinter import *
from Images.create_images import *
from stack import *
import sqlite3

global stack3Dict
stack3Dict = {}
createCardStack3(stack3Dict, 'pile_3')
global stack2Dict
stack2Dict = {}
createCardStack2(stack2Dict, 'pile_2')
global stack1Dict
stack1Dict = {}
createCardStack1(stack1Dict, 'pile_1')

class Bank:
  def __init__(self, root):
    self.root = root
    self.stack_cards_1 = Stack()
    self.stack_cards_2 = Stack()
    self.stack_cards_3 = Stack()
    self.stack_nobles = Stack()
    self.list_token = None


  def updateTokenDisplay(self):
    t = ['diamond', 'onyx', 'ruby', 'sapphire', 'emerald']
    for i in range(len(t)):
      lbToken = Label(self.root, text=self.list_token[t[i]], bg='#111111', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), height=1)
      lbToken.place(x=134+i*57, y=346, anchor=SW)
    lbToken = Label(self.root, text=self.list_token['gold'], bg='#111111', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), height=1)
    lbToken.place(x=448, y=346, anchor=SE)


  def displayBank(self):
    frStack3 = Frame(self.root, width=58, height=83)
    frStack3.place(x=53, y=13)
    lbStack3 = Label(frStack3, image=stack3Dict['pile_3'], justify=LEFT, width=60)
    lbStack3.place(x=-8, y=-1)
    frStack2 = Frame(self.root, width=58, height=83)
    frStack2.place(x=53, y=104)
    lbStack2 = Label(frStack2, image=stack2Dict['pile_2'], justify=LEFT, width=60)
    lbStack2.place(x=-8, y=-1)
    frStack1 = Frame(self.root, width=58, height=83)
    frStack1.place(x=53, y=196)
    lbStack1 = Label(frStack1, image=stack1Dict['pile_1'], justify=LEFT, width=60)
    lbStack1.place(x=-9, y=-3)
    self.updateTokenDisplay()


  def adjust_tokens(self, nb_players):
    if nb_players == 2:
      self.list_token = {'ruby':4, 'diamond':4, 'onyx':4, 'sapphire':4, 'emerald':4, 'gold':5}
    elif nb_players == 3:
      self.list_token = {'ruby':5, 'diamond':5, 'onyx':5, 'sapphire':5, 'emerald':5, 'gold':5}
    elif nb_players == 4:
      self.list_token = {'ruby':7, 'diamond':7, 'onyx':7, 'sapphire':7, 'emerald':7, 'gold':5}


  def create_stack_cards(self):
    for i in range(0, 4):
      conn = sqlite3.connect(f'sql/stack_cards_{i}.db')
      c = conn.cursor()
      c.execute(f"SELECT name FROM stack_cards_{i}")
      for name in c.fetchall():
        name = name[0]
        if i == 0:
          self.stack_nobles.stack(name)
        elif i == 1:
          self.stack_cards_1.stack(name)
        elif i == 2:
          self.stack_cards_2.stack(name)
        elif i == 3:
          self.stack_cards_3.stack(name)
      conn.commit()
      conn.close()

  def verify_token_possession(self, list):
    for elt in list:
      if self.list_token[elt] == 0:
        return False
    return True

  def remove_tokens_content(self, list):
    for elt in list:
      self.list_token[elt] -= 1

  def add_tokens(self, token, number):
    self.list_token[token] += number


  def cost_card(self, card, deck):
    conn = sqlite3.connect(f'sql/stack_cards_{deck}.db')
    c = conn.cursor()
    c.execute(f"SELECT cost_d, cost_s, cost_e, cost_r, cost_o FROM stack_cards_{deck} WHERE name='{card}'")
    all = c.fetchall()
    conn.commit()
    conn.close()
    return all

  def prestige(self, card, deck):
    conn = sqlite3.connect(f'sql/stack_cards_{deck}.db')
    c = conn.cursor()
    c.execute(f"SELECT prestige FROM stack_cards_{deck} WHERE name='{card}'")
    p = c.fetchall()
    conn.commit()
    conn.close()
    print('icic', p)
    return p[0][0]

  def give_card(self, card, deck):
    conn = sqlite3.connect(f'sql/stack_cards_{deck}.db')
    c = conn.cursor()
    c.execute(f"SELECT give_d, give_s, give_e, give_r, give_o FROM stack_cards_{deck} WHERE name='{card}'")
    all = c.fetchall()
    conn.commit()
    conn.close()
    return all

  def give_noble(self, list, board):
    conn = sqlite3.connect(f'sql/stack_cards_0.db')
    c = conn.cursor()
    c.execute(f"SELECT name FROM stack_cards_0 WHERE cost_d<={list['diamond']} AND cost_s<={list['sapphire']} AND cost_e<={list['emerald']} AND cost_r<={list['ruby']} AND cost_o<={list['onyx']} AND (name='{board.list_nobles[0]}' OR name='{board.list_nobles[1]}' OR name='{board.list_nobles[2]}')")
    all = c.fetchall()
    conn.commit()
    conn.close()
    return all
    

  def shuffle_decks(self):
    self.stack_cards_1.shuffle()
    self.stack_cards_2.shuffle()
    self.stack_cards_3.shuffle()
    self.stack_nobles.shuffle()