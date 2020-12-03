#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:40:46 2020

@author: aditya
"""

import nltk

def Tokenize_space(inp):
    nltk_tokens = nltk.word_tokenize(inp)
    return nltk_tokens