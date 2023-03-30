def verify_3_tokens(word):
  if len(word) == 5:
    if ',' in word:
      word = word.split(',')
      for elt in word:
        if elt not in ['r', 'd', 'o', 's', 'e']:
          return False
      if word[0] == word[1] or word[0] == word[2] or word[1] == word[2]:
        return False
      return True
  return False

def verify_2_tokens(word):
  if word in ['r', 'd', 'o', 's', 'e']:
    return True
  return False


def associate_letter(letter):
  d = {'r':'ruby', 'd':'diamond', 'o':'onyx', 'e':'emerald', 's':'sapphire'}
  return d[letter]