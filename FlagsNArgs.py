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


def look_for_main_arg(inp):
    mainarg = ""
    tokens = Tokenize_space(inp)
    i = 1
    token = tokens[i]
    while (token[0] != '-'):
        mainarg  =mainarg+token+" "
        i = i+1
        token = tokens[i]
    mainarg = mainarg.strip()
    return mainarg
    

def look_for_flag_arg_pair(inp):
    flag_arg_pair = {}
    tokens = Tokenize_space(inp)
    for token in tokens:
        if(token[0] == '-'):
            flag_arg_pair[token] = ""
    
    for x in range(1,len(tokens)):
        if tokens[x][0] == "-":
            i=1
            finalarg = ""
            if(x+i<len(tokens)):
                temparg = tokens[x+i]
            else:
                break
            while(temparg[0] != '-'):
                finalarg = finalarg + temparg + " "
                i = i+1
                if(x+i<len(tokens)):
                    temparg = tokens[x+i]
                else:
                    break
            flag_arg_pair[tokens[x]] = finalarg.strip()
            
    return flag_arg_pair



# try1 = "wishlist diwali wish -s -a hello world -r valorant part 2"
# ans = look_for_flag_arg_pair(try1)
# print(ans)
            