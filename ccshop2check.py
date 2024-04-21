# ⚙️ Format: CCnum|Exp.Date|CVV|Address|Zip|
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
            c = ウ.split('<td class="text-start">')[1].split('|')
            cc = c[0].strip(' ')
            exp = f'{c[1].rstrip()}{c[2].lstrip().replace('20','')}'.strip(' ')
            cvv = c[3].strip(' ')
            addr = ''; err = ''
            if c[6] != '  ':
               if any(i.isdigit() for i in c[6]):
                  addr = c[6].lstrip().rstrip()
               else: # too lazy to support uncommon base values
                err = '[!] no street / zip found, possibly from base with different amount of values'
            if addr == '': # apparently does not support zip only,
               zip = '' # requires street if checking with addr+zip option (because of avs according to dev)
               err = '[!] no street / zip found, possibly from base with different amount of values'
            if c[9] != '  ' and addr != '': zip = c[9].strip(' ')
            log = f'{cc}|{exp}|{cvv}|{addr}|{zip}|{err}'
            if err != '': invalid += [log]
            else: valid += [log]
    for v in valid: print(v)
    for iv in invalid: print(iv)
ミ=tk.Button(ー, text="Click here to input the html source", command=ァ)
ミ.pack();ー.mainloop()
