class Cell:
  def __init__(self, v, s):
    self.value = v
    self.next = s

  def __repr__(self):
    return 'Cell object: ' + str(self.value) + ' : ' + str(self.next)

  #peut etre garder
  def inverse(self):
    self2 = None
    for _ in range(self.length()):
      self2 = Cell(self.value, self2)
      self = self.next
    return self2













































    

  def affiche(self):
    self2 = self
    while self2 is not None:
      print(self2.value, end=" ")
      self2 = self2.next
    print()

