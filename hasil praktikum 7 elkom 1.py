# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 09:17:38 2021

@author: sarah sakinah
"""

print("@@@@ @@@ @@@@ @@@  @ @")
print("@    @ @ @  @ @ @  @ @")
print("@    @@@ @@@@ @@@  @ @")
print("@@@@ @@@ @@   @ @  @@@")
print("   @ @ @ @ @  @ @  @ @")
print("   @ @ @ @  @ @ @  @ @")
print("@@@@ @ @ @   @@ @  @ @")

def faktorial(n):
    faktorial = 1
    
    for i in range(1,n + 1):
        faktorial = faktorial*i
    print("faktorial dari",n,"adalah",faktorial)
nilai = int(input("nilai: "))
faktorial(nilai)