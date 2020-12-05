#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 12:28:07 2020

@author: aditya
"""
import os
#import platform


def Clear(inp):
    if os.name == "posix":
        os.system("clear")   
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        print("Sorryy we dont currently support \"clear\" for your OS")
    return 1



  # else:
  #   # Fallback for other operating systems.
  #   print('\n' * numlines)