#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 22:04:21 2020

@author: aditya
"""


'''
Developer Notes :
    Function---------------Input---------------Return
    
    --------------------------------------------------------------------------
    Prompt_And_Read        void                User input
    
    ---------------------------------------------------------------------------  
    Tokenize_space         String              List of strings
    eg:
        Hello World , How   ->    ["Hello","World",",","How"]
    eg:
        Search Rainbow Six Siege   ->  ["Search","Rainbow","Six","Siege"]
        can access list od strings using iterator
        ! Notice List[0] will be the name of function
        
   ----------------------------------------------------------------------------
    is_builtin            List[0]              i if List[0] is builtin function
                                               (i is the index of the function)
                                              -1 if it isn't a builtin function
    eg:
        search    ->     0(because search is the 0th builtin function)
        aditya    ->    -1
    
    ---------------------------------------------------------------------------
    
    *----This was all for the basic tokenizing-----*
    --------------------------------------------------------------------------
    Now example of a builtin-function
    Search:
        Now that we have noted that the first element of the list ie List[0]
        is search now we will have to take care of the rest of the input
        
        it can be <Arguments>   or  <Short Flags>   or   <Long Flags>:
            <Arguments>:
                Arguments are basically the input for the builting function 
                that we will be running like search Mario here Mario is the 
                argument
            <Short Flags>:
                These are basically the specifications in which a function 
                needs to be run they are mentioned in a single char
                like -a would mean that search for AAA games only
                or -r would mean that the game is released 
                however a point worth noting is -ar and -a -r will be the same 
                so "search Mario -ar" and "search Mario -a -r" would both give 
                same results
                Redundant flags: There is no flag as -x defined for search 
                function so there will be no effect on our execution there is 
                no need to send an error 
                so basically "-axxxr" and "-a -x -y -r" and "-ar" are same
            <Long Flags>:   (Yet to implement)
                These are basically easy to remember flag names which are most 
                frequently used However they are different from Short flags as 
                they are preceeded by --
                like search Mario --is_aaa and search Mario -a are same 
                however long flags can't be compunded like short flags
                so WRONG!  -> --is_aaais_cracked wont work
                also an error message needs to be sent on encountering wrong 
                long flag
                
            Now that we understand what the rest of the list can contain we 
            plan on setting some integers indicators based on the flags
            
                
                
    
    

'''