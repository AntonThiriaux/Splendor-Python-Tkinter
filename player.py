from tkinter import *
from Images.create_images import *

global tokenDict
tokenDict = {}
tab = ['ruby_token', 'diamond_token', 'onyx_token', 'sapphire_token', 'emerald_token', 'gold_token']
for elt in tab:
  createTokenImage(tokenDict, elt)

def getHandImage(name, deck):
  return createHandImage(name, deck)

class Player:
  def __init__(self, root, name, id):
    self.frame = Frame(root, width=150, height=405, bg='#0557a2')
    self.frame.place(x=570, y=0) #width=80, height=40, 
    self.button = Button(root, text=f'{name}', font=("Century Gothic", 10), width=10, relief=FLAT, bg='#3c272f', fg='#FFFFFF', activebackground='#3c272f', activeforeground='#FFFFFF', highlightbackground='#3c272f', command=lambda *args: self.displayPlayer())
    self.button.place(x=30+(id-1)*130, y=360)
    self.token = {'ruby':0, 'diamond':0, 'onyx':0, 'sapphire':0, 'emerald':0, 'gold':0}
    self.token_dev = {'ruby':0, 'diamond':0, 'onyx':0, 'sapphire':0, 'emerald':0}
    self.cards = {'nobles':[], 'development':[]}
    self.prestige = 0
    self.hand = [1, '0_d_1r_1s_1o_1v']
    self.name = name
    self.id = id


  def displayPlayer(self):
    self.frame.tkraise()
    for widget in self.frame.winfo_children():
      widget.destroy()
    lbPlayerName = Label(self.frame, text=f'Joueur #{self.id}: {self.name}', width=20, height=2, fg='#FFFFFF', bg='#3c272f')
    lbPlayerName.place(x=75, y=0, anchor=N)
    lbTokenInfo = Label(self.frame, text='Tokens   | Tokens Bonus', bg='#0557a2', fg='#FFFFFF')
    lbTokenInfo.place(x=1, y=40)
    lbRuby = Label(self.frame, image=tokenDict['ruby_token'], text=f"  {self.token['ruby']}  |    {self.token_dev['ruby']}", compound=LEFT, bg='#0557a2', fg='#FFFFFF')
    lbRuby.place(x=5, y=60)
    lbDiamond = Label(self.frame, image=tokenDict['diamond_token'], text=f"  {self.token['diamond']}  |    {self.token_dev['diamond']}", compound=LEFT, bg='#0557a2', fg='#FFFFFF')
    lbDiamond.place(x=5, y=90)
    lbEmerald = Label(self.frame, image=tokenDict['emerald_token'], text=f"  {self.token['emerald']}  |    {self.token_dev['emerald']}", compound=LEFT, bg='#0557a2', fg='#FFFFFF')
    lbEmerald.place(x=5, y=120)
    lbSapphire = Label(self.frame, image=tokenDict['sapphire_token'], text=f"  {self.token['sapphire']}  |    {self.token_dev['sapphire']}", compound=LEFT, bg='#0557a2', fg='#FFFFFF')
    lbSapphire.place(x=5, y=150)
    lbOnyx = Label(self.frame, image=tokenDict['onyx_token'], text=f"  {self.token['onyx']}  |    {self.token_dev['onyx']}", compound=LEFT, bg='#0557a2', fg='#FFFFFF')
    lbOnyx.place(x=5, y=180)
    #lbSeperatorLine = Label(self.frame, text='____________________________________', font=('Arial', 12, 'bold'), bg='#0557a2', fg='#FFFFFF')
    #lbSeperatorLine.place(x=-2, y=219)
    lbGold = Label(self.frame, image=tokenDict['gold_token'], text=f"  {self.token['gold']}", compound=LEFT, bg='#0557a2', fg='#FFFFFF')
    lbGold.place(x=5, y=213)
    lbHand = Label(self.frame, text=f'Cartes Réservée(s) - {len(self.hand)//2}/3:', bg='#0557a2', fg='#FFFFFF')
    lbHand.place(x=0, y=245)
    for i in range(1, len(self.hand), 2):
      image = getHandImage(self.hand[i], self.hand[i-1])
      lbCard = Label(self.frame, image=image, bg='#0557a2')
      lbCard.image = image
      lbCard.place(x=2+24*(i-1), y=325, anchor=SW)
    lbPlayerInfo = Label(self.frame, text=f"Points de prestige: {self.prestige}\nNombre de cartes\n  - Dévelopement: {len(self.cards['development'])}\n  - Nobles            : {len(self.cards['nobles'])}", bg='#0557a2', fg='#FFFFFF', justify=LEFT)
    lbPlayerInfo.place(x=5, y=395, anchor=SW)
    

    

  def __repr__(self):
    return str(self.name) + '|' + str(self.id)

  def add_tokens(self, list):
    for elt in list:
      self.token[elt] += 1
    

  def affichage_liste(self, list):
    content = ''
    for i in range(len(list)):
      content = content + ' | ' + str(list[i])
    content = content + ' | '
    return content

  def affichage_dict(self, dict):
    content = ''
    for elt in dict.keys():
      content = content + ' | ' + elt + ': ' + str(dict[elt])
    content = content + ' | '
    return content


  def verify_pay(self, list, bank):
    tokens = ['diamond', 'sapphire', 'emerald', 'ruby', 'onyx']
    sum = 0
    for i in range(len(tokens)):
      if self.token_dev[tokens[i]] + self.token[tokens[i]] - list[i] < 0:
        sum += self.token_dev[tokens[i]] + self.token[tokens[i]] - list[i]
    if self.token['gold'] + sum < 0:
      return False
    #return True
    #verifier dans la capacite de payer
    else:
      l = []
      for i in range(len(tokens)):
        if self.token_dev[tokens[i]] - list[i] < 0:
          l.append(tokens[i])
          l.append(self.token_dev[tokens[i]] - list[i])
      sum = 0
      for i in range(len(l)//2):
        if self.token[l[i*2]] + l[i*2+1] < 0:
          sum += self.token[l[i*2]] + l[i*2+1]
          while self.token[l[i*2]] > 0:
            self.token[l[i*2]] -= 1
            bank.add_tokens(l[i*2], 1)
        else:
          self.token[l[i*2]] += l[i*2+1]
          bank.add_tokens(l[i*2], -l[i*2+1])
      self.token['gold'] += sum
      bank.add_tokens('gold', -sum)
      return True

    

  def update_dev(self, list):
    tokens = ['diamond', 'sapphire', 'emerald', 'ruby', 'onyx']
    for i in range(len(tokens)):
      self.token_dev[tokens[i]] += list[i]


  def affiche(self):
    print('='*120)
    print('Player  : ', self.name)
    print('Tokens  : ', self.affichage_dict(self.token))
    print('Prestige: ', self.prestige)
    print('-'*120)
    print('Cards   : ', self.affichage_dict(self.cards))
    print('Bonuses : ', self.affichage_dict(self.token_dev))
    print('Hand    : ', self.affichage_liste(self.hand))
    print('='*120)