from tkinter import *

main_root = Tk()
main_root.geometry('720x405')
main_root.overrideredirect(True)

from Images.create_images import *

from selection import *
from rules import *



def rules_page():
  rules_window = Toplevel()
  rules_display(rules_window)


def playGame():
  infoRoot = Toplevel()
  numberOfPlayers(infoRoot)






menu_images = {}
tab = [('splendor_background', 720, 405), ('play_button_image', 250, 70), ('rules_button_image', 50, 50), ('quit_button_image', 35, 35)]

for elt in tab:
  create_images_menu(menu_images, elt[0], elt[1], elt[2])













root_background = Label(main_root, image=menu_images['splendor_background'])
root_background.place(x=-1, y=-1)

bt_play = Button(main_root, image=menu_images['play_button_image'], relief=FLAT, highlightthickness=0, borderwidth=0, border=0, bg='#252b37', activebackground='#252b37', command=playGame)
bt_play.place(x=500, y=310, anchor=CENTER)

bt_rules = Button(main_root, image=menu_images['rules_button_image'], relief=FLAT, highlightthickness=0, borderwidth=0, border=0, bg='#21263d', activebackground='#21263d', command=rules_page)
bt_rules.place(x=710, y=395, anchor=SE)

bt_erase = Button(main_root, image=menu_images['quit_button_image'], relief=FLAT, highlightthickness=0, borderwidth=0, border=0, bg='#435a73', activebackground='#435a73', command=lambda: main_root.destroy())
bt_erase.place(x=710, y=10, anchor=NE)





main_root.mainloop()