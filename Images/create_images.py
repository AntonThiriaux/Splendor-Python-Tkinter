from tkinter import *
from PIL import ImageTk
#from PIL import Image
import PIL.Image


def create_images_menu(dict, name, width, height):
  dict[name] = PIL.Image.open(f"Images/menu_images/{name}.png")
  dict[name] = dict[name].resize((width, height))
  dict[name] = ImageTk.PhotoImage(dict[name])

def createSingleImage(name, width, height):
  image = PIL.Image.open(f"Images/menu_images/{name}.png")
  image = image.resize((width, height))
  image = ImageTk.PhotoImage(image)
  return image

def createTokenImage(dict, name):
  dict[name] = PIL.Image.open(f"Images/tokens/{name}.png")
  dict[name] = dict[name].resize((25, 25))
  dict[name] = ImageTk.PhotoImage(dict[name])

def createHandImage(name, deck):
  image = PIL.Image.open(f"Images/Cartes_{deck}_point/{name}.png")
  image = image.resize((50, 50))
  image = ImageTk.PhotoImage(image)
  return image

def createCardStack3(dict, name):
  dict[name] = PIL.Image.open(f"Images/Cartes_3_point/{name}.png")
  dict[name] = dict[name].resize((73, 83))
  dict[name] = ImageTk.PhotoImage(dict[name])

def createCardStack2(dict, name):
  dict[name] = PIL.Image.open(f"Images/Cartes_2_point/{name}.png")
  dict[name] = dict[name].resize((73, 84))
  dict[name] = ImageTk.PhotoImage(dict[name])

def createCardStack1(dict, name):
  dict[name] = PIL.Image.open(f"Images/Cartes_1_point/{name}.png")
  dict[name] = dict[name].resize((75, 87))
  dict[name] = ImageTk.PhotoImage(dict[name])

def createImageInList(name, deck):
  image = PIL.Image.open(f"Images/Cartes_{deck}_point/{name}.png")
  image = image.resize((73, 84))
  image = ImageTk.PhotoImage(image)
  return image