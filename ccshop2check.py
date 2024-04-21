import tkinter as tk
from tkinter import simpledialog
root = tk.Tk(); root.title('🦎')
def ァ():
    ア = simpledialog.askstring("ccshop2check", "paste the html from view-source:https://ccshop2.com/cc_list.php (check your terminal for the output)")
    if ア:
       イ = ア.split('\n')
       for ウ in イ:
           if '<td class="text-start">' in ウ:
            card = ウ.split('<td class="text-start">')[1].split('|')
            cc = card[0].strip(' ')
            exp = f'{card[1].rstrip()}{card[2].lstrip().replace('20','')}'.strip(' ')
            cvv = card[3].strip(' ')
            addr = ''
            if card[6] != '  ': addr = card[6].lstrip().rstrip()
            zip = ''
            if card[9] != '  ': zip = card[9].strip(' ')
            print(f'{cc}|{exp}|{cvv}|{addr}|{zip}|')
button = tk.Button(root, text="Click here to input the html source", command=ァ)
button.pack()
root.mainloop()
