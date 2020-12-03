#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:40:00 2020

@author: aditya
"""

from Tokenize import Tokenize_space

def look_for_flags(inp):
    flags = ""
    tokens = Tokenize_space(inp)
    for x in tokens:
        if (x[0] == '-'):
            for i in range (1,len(x)):
                flags = flags+x[i]
    return flags

def look_for_arguments(inp):
    arguments = ""
    tokens = Tokenize_space(inp)
    for x in range(1,len(tokens)):
        if (tokens[x][0] != '-'):
            arguments = arguments+tokens[x]+" "
    return arguments