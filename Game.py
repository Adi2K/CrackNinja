#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:01:31 2020

@author: aditya
"""


class Game:
    def __init__(self, name, status = "N.A.", crackedafter = "N.A.", releasedate = "N.A.", crackdate = "N.A.", drm = "N.A.", scenegroup = "N.A.", price_dict = "N.A.", followers = "N.A.",link = "N.A."):
        self.name = name
        self.status = status
        self.crackedafter = crackedafter
        self.releasedate = releasedate
        self.crackdate = crackdate
        self.drm = drm
        self.scenegroup = scenegroup
        self.price_dict = price_dict
        self.followers = followers
        self.link = link
      
    
    def myname(self):
        print("Game Name : " + self.name)
    
    def mystatus(self):
        print("Game Status : "+ self.status)
  
    
    

# p1 = Game("Rainbow Six Siege","Cracked")
# p1.myname()
# p1.mystatus()


