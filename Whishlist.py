

import os
from FlagsNArgs import look_for_main_arg, look_for_flag_arg_pair 
from Search import crackninjaSearch

#from Tokenize import Tokenize_space

def Whishlist(inp):
    
    file_name = look_for_main_arg(inp)
    file_name = file_name + ".txt"
    
    if (file_name == ".txt"):
        file_name = "wishlist.txt"
    
    fna = look_for_flag_arg_pair(inp)
    
    
    
    for df, dn in fna.items():
        
        if(df == "-a"):
            
            ans = crackninjaSearch(dn)
            dn = ans.myname()
            
            return Add_to_wishlist(file_name,dn)
            
            
        elif(df == "-r"):
            
            return Remove_from_wishlist(file_name,dn)
            
        elif(df == "-s"):
            
            return Show_wishlist(file_name)
            
    

def Add_to_wishlist(file_name,Game_name):
      
    WishList_File_object=open(file_name,"a")

    if(check_if_string_in_file(file_name, Game_name)):
        print("This game is already added to your wishlist")
        return 1
    else:
        WishList_File_object.write(Game_name+"\n")
        print(Game_name," has been added to your wishlist")
        return 1

    
    



def Remove_from_wishlist(file_name,Game_name):
    PATH = "./"+file_name
    if os.path.isfile(PATH) and os.access(PATH, os.W_OK):
        if(check_if_string_in_file(file_name,Game_name)):
            with open(file_name, "r") as f: 

                data = f.readlines() 
            # open file in write mode 
            with open(file_name, "w") as f: 
              
                for line in data : 
                  
                # condition for data to be deleted 
                    if line.strip("\n") != Game_name:  
                        f.write(line)
                print(Game_name+" has been removed from your wishlist")
            return 1
        else:
            print(Game_name," is not present in your wishlist")
            Show_wishlist(file_name)
            print("Select the game to be removed")
            return 1
    else:
        print("No such Whishlist is present")
        return 1
 #***************Function for printing wishlist****************   
        
    

def Show_wishlist(file_name):
    
    PATH = "./"+file_name
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        if os.stat(file_name).st_size == 0:
            print("Your wishlist is empty")
            return 1
        else:
            print("Whishlist : ",file_name)
            WishList_File_object=open(file_name,"r")
            game_list = (WishList_File_object.readlines())
            for game in game_list:
                name = game.strip(" \n")
                print(name)
            return 1
    else:
        print("No such Whishlist is present")
        return 1
    


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



