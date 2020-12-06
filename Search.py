#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:39:14 2020

@author: aditya
"""

from FlagsNArgs import look_for_arguments, look_for_flags
from Search_scrape import search_scrape
from scrap import search_game
from Game import Game


def Search(inp):
    flag_list = set_search_flags((look_for_flags(inp)))
    name = look_for_arguments(inp)
    ans = crackninjaSearch(name,0,flag_list[0],flag_list[1],flag_list[2],flag_list[3],flag_list[4],flag_list[5])
    if(ans == 1):
        return 1
    ans.printdetails()
    return 1



def set_search_flags(flags):
    flags_of_search = ["a","i","c","n","r","u"]
    num_flags_of_search = 6
    flag_list = [True,True,True,True,True,True]
    flagset_list = [False,False,False,False,False,False]
    for f in flags:
        #print(f)
        for i in range (num_flags_of_search):
             if (f == flags_of_search[i]):
                if (i%2 ==0):
                    flag_list[i] = True
                    flagset_list[i] = True
                    flag_list[i+1] = not(flagset_list[i] ^ flagset_list[i+1])
                else:
                    flag_list[i] = True
                    flagset_list[i] = True
                    flag_list[i-1] = not(flagset_list[i] ^ flagset_list[i-1])
    return flag_list



def crackninjaSearch(name,number =10,is_aaa = True, is_indie =True, is_cracked = True, is_notcracked = True, is_released = True, is_unreleased = True ):

    #yaha pe pura scrapping vagera call hoga 
    if(is_aaa and is_indie):
        gtype = 0
    elif(is_aaa):
        gtype = 1
    elif(is_indie):
        gtype = 2
        
    if(is_cracked and is_notcracked):
        gstatus = 0
    elif(is_cracked):
        gstatus = 1
    elif(is_notcracked):
        gstatus = 2
    
    if(is_released and is_unreleased):
        grel_d = 0
    elif(is_released):
        grel_d = 1
    elif(is_unreleased):
        grel_d = 2

        
    ans = search_scrape(name,gstatus,grel_d,gtype)
    display = {}
    i = 1
    for a in ans.keys():
        display[i] = a
        i = i+1
    
    print("\n","---------RESULT--------")
    for dk, dv in display.items():
        print(dk,"-->",dv)

    print("\n"," Choose the index of the Game you want OR 0 to go back: ") 
    valid = 0    
    while(not valid):
        choice = input("   >>")
        if(choice.isnumeric()):
            if(int(choice) >= 0 and int(choice) < i):
                valid = 1
            else:
                print("    Sorry, Please make a VALID choice !")
        else:
            print("    Sorry, Please make a VALID choice !")
    
    if(int(choice) == 0):
        return 1
    
    link = ans[display[int(choice)]]
    
    game_res = search_game(link)
    return game_res
