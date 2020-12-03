#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:56:21 2020

@author: aditya
"""

from Builtin import builtin_methods_name
from FlagsNArgs import look_for_flags



def Help(inp):
    flags_of_help = builtin_methods_name[:]
    flag = look_for_flags(inp)
    if (flag == ""):
             print("Here is a list of all the bulitin Methods of CrackNinja")
             for m in builtin_methods_name:
                    print(m)
    
             print("\n","You can try \"help -search\" to get help on Search method.")
             return 1
    else:
        for i in range (len(flags_of_help)):
            if (flag == flags_of_help[i]):
                method = i
                break
            else:
                method = -1
        #print(method)
        if (method == -1):
            print("No Such Method entry in Help documentation")
        elif (method == 1):
            print("")
            print("Help Documentation of ",flags_of_help[method])
            print("Blah...... Blah....... Blah.......")
        elif (method == 2):
            print("")
            print("Help Documentation of ",flags_of_help[method])
            print("Blah...... Blah....... Blah.......")
        else:
            print("")
            print("Help Documentation of ",flags_of_help[method])
            print("Blah...... Blah....... Blah.......")
        return 1
    
    