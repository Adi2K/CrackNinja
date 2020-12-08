#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:21:00 2020

@author: aditya
"""
from chrome_b import chrome_browser


def Exit(inp):
    chrome_browser.quit()
    return 0