import tkinter as tk
from tkinter import simpledialog
ー=tk.Tk();ー.title('🦎')
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
            addr = ''; err = ''
            if card[6] != '  ':
               if any(i.isdigit() for i in card[6]):
                  addr = card[6].lstrip().rstrip()
               else: # too lazy to support uncommon base values
                err = '[!] no street # found, possibly from base with different amount of values'
            if addr == '': zip = '' # apparently does not support zip only, requires street if checking with addr+zip option (according to dev)
            if card[9] != '  ' and addr != '': zip = card[9].strip(' ')
            print(f'{cc}|{exp}|{cvv}|{addr}|{zip}|{err}')
ミ=tk.Button(ー, text="Click here to input the html source", command=ァ)
ミ.pack();ー.mainloop()
