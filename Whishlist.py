#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:19:28 2020

@author: aditya
"""
import os

from Tokenize import Tokenize_space

def Add_Whishlist(inp):
    Game_name = ""
    Args_tokens=Tokenize_space(inp)
    Args_tokens.pop(0)
       
    for i in (Args_tokens):
        if(i[0]!='-'):
            Game_name=Game_name+i+" "
    f="wishlist.txt"       
    WishList_File_object=open(f,"a")

    if(check_if_string_in_file(f, Game_name)):
        print("This game is already added to your wishlist")
        return 1
    else:
        WishList_File_object.write(Game_name+"\n")
        print("You are trying to run whishlist")
        return 1
            
            
#***********Remove from wishlist******************
    
    #delete_string(Game_name)
    #return 1
            
            
 #**********Show wishlist********************   
    #show_wishlist()
    #return 1
    
    
#***********Function for checking String in a File******************
        
def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False 

 #***************Function for deleting a string from file***********

def delete_string(file_name,Game_name):
    with open(file_name, "r") as f: 
      
    # read data line by line  
        data = f.readlines() 
      
    # open file in write mode 
    with open(file_name, "w") as f: 
      
        for line in data : 
          
        # condition for data to be deleted 
            if line.strip("\n") != name:  
                f.write(line)
        print(Game_name+"has been removed from your wishlist")
 #***************Function for printing wishlist****************   
        
def show_wishlist(file_name):
    WishList_File_object=open(file_name,"r")
    game_list = (WishList_File_object.readlines())
    print("Your wishlist :")
    for game in game_list:
       name = game.strip(" \n")
       print(name)
 
#import os
#file_path = 'mysample.txt'
# check if size of file is 0
#if os.stat(file_path).st_size == 0:
    #print('File is empty')

#else:
    #print('File is not empty')   
    
