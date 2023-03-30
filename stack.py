from random import randint
from cell import *

class Stack:
  def __init__(self):
    self.content = Cell(None, None)

  def length(self):
    self2 = self.content
    if self2.value == None:
      return 0
    len = 1
    while self2.next is not None:
      self2 = self2.next
      len += 1
    return len

  def unstack(self):
    #print(self)
    value = self.content.value
    self.content = self.content.next
    return value

  def __repr__(self):
    return str(self.content)

  #Peut etre garder
  def __getitem__(self, index):
    if 0 > index >= self.length():
      raise IndexError("Cell index out of range!")
    self2 = Stack()
    while index != 0:
      index -= 1
      self2.stack(self.unstack())
    value = self.unstack()
    self.stack(value)
    while self2.length() != 0:
      self.stack(self2.unstack())
    return value

  def stack(self, value):
    self.content = Cell(value, self.content)

  def shuffle(self):
    nb_times = randint(45, 90)
    for _ in range(nb_times):
      random_nb_1 = randint(0, self.length()-2)
      random_nb_2 = randint(0, self.length()-2)
      while random_nb_2 == random_nb_1:
        random_nb_2 = randint(0,self.length()-2)
      self.permutation(random_nb_1, random_nb_2)

  def is_empty(self):
    return self.content == None

  def affiche(self):
    self2 = self.content
    while self2 is not None:
      if self2.value != None:
        print(self2.value, end=" | ")
      self2 = self2.next
    print()

  def replace(self, index, value):
    if 0 > index >= self.length():
      raise IndexError('Cell index out of range')
    else:
      self2 = Stack()
      i = 0
      while i != index:
        i += 1
        v = self.unstack()
        self2.stack(v)
      self2.stack(value)
      self.unstack()
      while self2.length() != 0:
        v2 = self2.unstack()
        self.stack(v2)
      return self


  def permutation(self, index1, index2):
    value1 = self[index1]
    self.replace(index1, self[index2])
    self.replace(index2, value1)
