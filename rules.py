from tkinter import *
from Images.create_images import *

rules_image = {}
t = [('left_back_image', 40, 20), ('right_back_image', 40, 20), ('quit_button_image', 27, 27)]
tab = ['rules_page_1', 'rules_page_2', 'rules_page_3', 'rules_page_4', 'rules_page_5']

for elt in t:
  create_images_menu(rules_image, elt[0], elt[1], elt[2])

for elt in tab:
  create_images_menu(rules_image, elt, 720, 405)

def rules_display(root):
  root.geometry('720x405')
  root.overrideredirect(True)
  global i
  i = 1
  rules_page = Label(root, image=rules_image[f'rules_page_{i}'])
  rules_page.place(x=-1, y=-1)
  lbPageNumber = Label(root, text=f'{i}/5', fg='#EFEFEF', bg='#182025', font=('Helvetica', 10))
  lbPageNumber.place(x=715, y=400, anchor=SE)
  btBack = Button(root, image=rules_image['left_back_image'], width=26, activebackground='#182025', bg='#182025', relief=FLAT, highlightthickness=0, borderwidth=0, border=0)
  btBack.place(x=2, y=213, anchor=W)
  btForward = Button(root, image=rules_image['right_back_image'], width=26, activebackground='#4485a9', bg='#4485a9', relief=FLAT, highlightthickness=0, borderwidth=0, border=0)
  btForward.place(x=718, y=213, anchor=E)

  def goBack(e):
    global i
    if i >= 2:
      i -= 1
      rules_page.config(image=rules_image[f'rules_page_{i}'])
      lbPageNumber.config(text=f"{i}/5")

  def goForward(e):
    global i
    if i <= 4:
      i += 1
      rules_page.config(image=rules_image[f'rules_page_{i}'])
      lbPageNumber.config(text=f"{i}/5")

  root.bind('<Left>', goBack)
  root.bind('<Right>', goForward)
  btBack.bind('<Button-1>', goBack)
  btForward.bind('<Button-1>', goForward)

  btLeave = Button(root, image=rules_image['quit_button_image'], relief=FLAT, highlightthickness=0, borderwidth=0, border=0, bg='#435a73', activebackground='#435a73', command=lambda: root.destroy())
  btLeave.place(x=2, y=2)