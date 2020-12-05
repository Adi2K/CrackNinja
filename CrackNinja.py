#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:03:23 2020

@author: aditya
"""


from Builtin import is_builtin
from Tokenize import Tokenize_space


from Search import Search
from Help import Help
from Whishlist import Whishlist
from Addtofav import AddToFav
from Exit import Exit
from Clear import Clear


methodDictionary = {0: Search, 1: Whishlist, 2: AddToFav, 3: Exit, 4: Help, 5: Clear}


def Prompt_And_Read():
    inp = input("CrackNinja > ")
    return inp


return_status = 1
print("")
print(" NOTE : CrackNinja is a Scrapper for Crackwatch it only tracks crack status and offers no download, torrent, or such")


while(return_status):
    
    inp = Prompt_And_Read()
    tokens = Tokenize_space(inp)
    ibi = is_builtin(tokens[0])
    if (ibi != -1):   
        run = methodDictionary[ibi]
        return_status = run(inp)
    else:
        print("No Such Function avaliable in CrackNinja")



