#⚙️ Format:   CCnum|Exp.Date|CVV|Address|Zip|
import tkinter as tk
from tkinter import simpledialog
ー=tk.Tk();ー.title('🦎')
def ァ():
    ア = simpledialog.askstring("ccshop2check", "paste the html from view-source:https://ccshop2.com/cc_list.php (check your terminal for the output)")
    if ア:
       イ = ア.split('\n')
       valid = []; invalid = []
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
                err = '[!] no street / zip found, possibly from base with different amount of values'
            if addr == '': # apparently does not support zip only,
               zip = '' # requires street if checking with addr+zip option (because of avs according to dev)
               err = '[!] no street / zip found, possibly from base with different amount of values'
            if card[9] != '  ' and addr != '': zip = card[9].strip(' ')
            log = f'{cc}|{exp}|{cvv}|{addr}|{zip}|{err}'
            if err != '': invalid += [log]
            else: valid += [log]
    for v in valid: print(v)
    for iv in invalid: print(iv)
ミ=tk.Button(ー, text="Click here to input the html source", command=ァ)
ミ.pack();ー.mainloop()
