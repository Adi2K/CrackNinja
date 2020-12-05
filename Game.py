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
        return self.name
    
    def mylink(self):
        return self.link
        
    def printdetails(self):
        print("Game Details => ")
        print("Game Name : " + self.name)
        print("Game Status : "+ self.status)
        print("Extra Status : "+ self.crackedafter)
        print("Release Date: "+ self.crackdate)
        print("DRM Protection : "+ self.drm)
        print("Scene Group : "+ self.scenegroup)
        print("Followers : "+ self.followers)
        print("Game Link :"+ self.link)
        
        print("Prices :")
        for p,q in self.price_dict.items():
            print(p,"->", q)
        
        
  
    
    

# p1 = Game("Rainbow Six Siege","Cracked")
# p1.myname()
# p1.mystatus()


