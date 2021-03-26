# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:19:14 2021

@author:priyam

"""

user_input = str(input("Enter a Phrase: "))
text = user_input.split()
s = " "
for i in text:
    s = s+str(i[0]).upper()
    
print("The acronym of above pharse is :" ,s)