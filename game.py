from tkinter import *
from player import Player
#from cell import Cell
from board import Board
from bank import Bank
from auxilaries import *


class Game:
  def __init__(self, root):
    self.root = root
    self.board = Board(self.root)
    self.bank = Bank(self.board.frame)
    self.players = {}

  def __repr__(self):
    return '\nThis is the game.'

  def launch(self, dict_player):
    self.root.geometry('720x405')
    self.root.overrideredirect(True)
    self.root.config(bg='#3c272f')
    self.bank.create_stack_cards()
    self.bank.shuffle_decks()
    self.players = dict_player
    self.bank.adjust_tokens(len(dict_player))
    self.board.place_cards(self.bank, len(self.players))


    
    self.board.list_stack_3 = ['4_o_7r', '5_e_7s_3e', '5_o_7r_3o', '5_s_7d_3s']
    self.bank.stack_cards_3.stack('4_r_6v_3r_3s')
    self.bank.stack_cards_3.stack('4_e_6s_3e_3d')
    
    self.board.displayBoard(self.testAction)
    self.startTest(1)
    #self.start(1)

  def startTest(self, num):
    self.player = self.players[f'player_{num}']
    self.player.button.config(highlightbackground='#FFFFFF', activebackground='#FFFFFF', activeforeground='#3c272f')
    self.bank.displayBank()

    

  def testAction(self, deck, nom):
    print(nom, self.player.name)
    self.player.hand.append(deck)
    self.player.hand.append(nom)
    print(self.player.hand)
    if deck == 3:
      self.board.list_stack_3[self.board.list_stack_3.index(nom)] = self.bank.stack_cards_3.unstack()
    self.board.displayBoard(self.testAction)
    self.player.displayPlayer()


  def displayGame(self):
    self.board.affiche(self.root, self.bank)
    

  def choices(self):
    print("(Type '1'): Take 3 gem tokens of different colors.\n(Type '2'): Take 2 gem tokens of the same color.\n(Type '3'): Reserve 1 development card and take 1 gold token.\n(Type '4'): Purchase 1 face-up development card from the table or a previously reserved one.")
    print('_'*120)

  def do_action(self, num, choice):
    if choice == 1:
      tokens = self.proposition_action_1()
      self.do_action_1(num, tokens)
    elif choice == 2:
      token = self.proposition_action_2(num)
      self.do_action_2(token)
    elif choice == 3:
      card = self.proposition_action_3(num)
      self.do_action_3(card)
    elif choice == 4:
      card = self.proposition_action_4()
      self.do_action_4(num, card[0], card[1])
    return True

  def proposition_action_1(self):
    print("\nYou chose to take several tokens. Enter the first letter followed by a comma in the prompt, ex: 'r,d,s' for a ruby, a diamond and a sapphire.")
    print()
    tokens = input('Enter your desired tokens: ')
    while not(verify_3_tokens(tokens)):
      tokens = input('Enter your desired tokens: ')
    tokens = tokens.split(',')
    return tokens

  def do_action_1(self, num, tokens):
    tokens = [associate_letter(tokens[0]), associate_letter(tokens[1]), associate_letter(tokens[2])]
    if not(self.bank.verify_token_possession(tokens)):
      return self.do_action(num, 1)
    self.bank.remove_tokens_content(tokens)
    self.player.add_tokens(tokens)


  def proposition_action_2(self, num):
    print("\nYou chose to take two same tokens. Enter the first letter in the prompt, ex: 'r' for a ruby.")
    print()
    tokens = input('Enter your desired token: ')
    while not(verify_2_tokens(tokens)):
      tokens = input('Enter your desired tokens: ')
    if self.bank.list_token[associate_letter(tokens)] >= 4:
      return associate_letter(tokens)
    return self.start(num)

  def do_action_2(self, token):
    self.bank.remove_tokens_content([token, token])
    self.player.add_tokens([token, token])
    return True

  def proposition_action_3(self, num):
    if self.bank.list_token['gold'] == 0 or len(self.player.hand) == 3:
      print('Error: action not possible.\n')
      return self.start(num)
    print("\nYou chose to reserve a development card. Enter the exact name of the card, ex: 'p4_d0_s3_e6_r3_o0'")
    print()
    card_name = input('Please enter the exact name of the card: ')
    while card_name not in self.board.list_stack_1 and card_name not in self.board.list_stack_2 and card_name not in self.board.list_stack_3:
      card_name = input('Please enter the exact name of the card: ')
    return card_name

  def do_action_3(self, card_name):
    if card_name in self.board.list_stack_1:
      self.board.list_stack_1.pop(self.board.list_stack_1.index(card_name))
      self.board.list_stack_1.append(self.bank.stack_cards_1.unstack())
      n = 1
    elif card_name in self.board.list_stack_2:
      self.board.list_stack_2.pop(self.board.list_stack_2.index(card_name))
      self.board.list_stack_2.append(self.bank.stack_cards_2.unstack())
      n = 2
    elif card_name in self.board.list_stack_3:
      self.board.list_stack_3.pop(self.board.list_stack_3.index(card_name))
      self.board.list_stack_3.append(self.bank.stack_cards_3.unstack())
      n = 3
    self.bank.list_token['gold'] -= 1
    self.player.hand.append(n)
    self.player.hand.append(card_name)
    self.player.token['gold'] += 1


  def proposition_action_4(self):
    print("\nYou chose to purchase a card. Enter the exact name of the card, ex: 'p4_d0_s3_e6_r3_o0'.")
    print()
    card_name = input('Please enter the name of the card: ')
    while card_name not in self.board.list_stack_1 and card_name not in self.board.list_stack_2 and card_name not in self.board.list_stack_3 and card_name not in self.player.hand:
      card_name = input('Please enter the exact name of the card: ')
    if card_name in self.board.list_stack_1:
      deck = 1
    elif card_name in self.board.list_stack_2:
      deck = 2
    elif card_name in self.board.list_stack_3:
      deck = 3
    else:
      if card_name in self.player.hand:
        deck = self.player.hand[self.player.hand.index(card_name)-1] + 10
    return card_name, deck
    

  def do_action_4(self, num, card, deck):
    if deck > 3:
      cost = self.bank.cost_card(card, deck-10)
    else:
      cost = self.bank.cost_card(card, deck)
    cost_card = []
    for elt in cost[0]:
      cost_card.append(elt)
    print(cost_card)
    if not self.player.verify_pay(cost_card, self.bank):
      print('\nYou do not have enough tokens to purchase the card!')
      return self.start(num)
    self.player.cards['development'].append(card)
    if deck > 3:
      prestige = self.bank.prestige(card, deck-10)
      give = self.bank.give_card(card, deck-10)
    else:
      prestige = self.bank.prestige(card, deck)
      give = self.bank.give_card(card, deck)
    give_card = []
    for elt in give[0]:
      give_card.append(elt)
    print(give_card)
    self.player.prestige += prestige
    self.player.update_dev(give_card)
    if deck > 3:
      index = self.player.hand.index(card)
      self.player.hand.pop(index)
      self.player.hand.pop(index-1)
    elif deck == 1:
      self.board.list_stack_1.pop(self.board.list_stack_1.index(card))
      self.board.list_stack_1.append(self.bank.stack_cards_1.unstack())
    elif deck == 2:
      self.board.list_stack_2.pop(self.board.list_stack_2.index(card))
      self.board.list_stack_2.append(self.bank.stack_cards_2.unstack())
    elif deck == 3:
      self.board.list_stack_3.pop(self.board.list_stack_3.index(card))
      self.board.list_stack_3.append(self.bank.stack_cards_3.unstack())
    
  def verify_win(self):
    return self.player.prestige >= 15

  def verify_sum_token(self):
    sum = 0
    for elt in self.player.token.keys():
      sum += self.player.token[elt]
    if sum > 10:
      print('\nYou have too many tokens! You can only have a maximum of 10 in total at the end of each turn.')
      while sum > 10:
        token = input('\nPlease enter the first letter of the token: ')
        while token not in ['d', 'r', 'g', 'o', 'e', 's']:
          token = input('\nPlease enter the first letter of the token: ')
        token = associate_letter(token)
        self.bank.list_token[token] += 1
        self.player.token[token] -= 1
        sum -= 1

  def noble_visit(self):
    nobles = self.bank.give_noble(self.player.token_dev, self.board)
    if nobles == []:
      return
    for i in range(len(nobles)):
      nobles[i] = nobles[i][0]
    if len(nobles) == 1:
      print('\nA noble has visited you! His name is', nobles[0])
      self.player.cards['nobles'].append(nobles[0])
      self.player.prestige += 3
      self.board.list_nobles.pop(self.board.list_nobles.index(nobles[0]))
    if len(nobles) > 1:
      print('Several nobles are visiting you. You must choose one too keep.')
      n = ''
      for elt in nobles:
        n = n + '  |  ' + elt
      print('Theses are the nobles:', n)
      noble = input('\nEnter the name of the noble you which to keep: ')
      while noble not in nobles:
        noble = input('\nEnter the name of the noble you which to keep: ')
      self.player.cards['nobles'].append(noble)
      self.player.prestige += 3
      self.board.list_nobles.pop(self.board.list_nobles.index(noble))
      

  def start(self, num):
    #print(num, self.nb_players)
    #print(self.dic_player)
    self.player = self.players[f'player_{num}']
    self.player.button.config(highlightbackground='#3c272f', activebackground='#FFFFFF', activeforeground='#3c272f')
    self.displayGame()
    #self.board.affiche(self.bank)
    #for elt in self.players.keys():
      #self.players[elt].affiche()
    print(f'\nHere are your choices {self.player.name}:')
    self.choices()
    choice = input('\nPlease enter the number corresponding to your choice: ')
    while choice not in ['1', '2', '3', '4']:
      choice = input('\nPlease enter the number corresponding to your choice: ')
    if self.do_action(num, int(choice)):
      self.verify_sum_token()
      self.noble_visit()
      if self.verify_win():
        print('Nice game!')
        return
      num = num % len(self.players) + 1
      print('\n\n\n\n')
      self.player.button.config(highlightbackground='#FFFFFF', activebackground='#3c272f', activeforeground='#FFFFFF')
      return self.start(num)
    print('\nThe action selected cannot be done, it is against the rules.\n\n\n\n')
    return self.start(num)