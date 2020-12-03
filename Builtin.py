#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:03:19 2020

@author: aditya
"""



#methodDictionary = {0: Search, 1: Whishlist, 2: AddToFav, 3: Exit, 4: Help}

builtin_methods_name = ["search", "whishlist", "addtofav", "exit", "help"]

num_builtin_methods = 5



#methodDictionary = {0: Search, 1: Whishlist, 2: AddToFav, 3: Exit, 4: Help}

def is_builtin(command):
    for i in range (num_builtin_methods):
        if (command == builtin_methods_name[i]):
            return i
    return -1