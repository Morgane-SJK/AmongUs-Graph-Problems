# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 17:58:05 2020

@author: Morgane
"""

import sys

import Part_1
import Part_2
import Part_3
import Part_4


def menu():
    print("""--- Final Project Advanced Data Structures and Algorithms ---
        1: Part 1
        2: Part 2
        3: Part 3
        4: Part 4
        Q: Quit/Log Out""")
    choice=input("Please enter your choice : ")
    while (choice!="Q" and choice!="q"):    
        if choice == "1":
            Part_1.main()
    
        elif choice == "2":
            Part_2.main()
    
        elif choice == "3":
            Part_3.main()
    
        elif choice == "4":
            Part_4.main()
    
        elif choice == "Q" or choice == "q":
            sys.exit
            
        else:
            print("You must only select either 1,2,3,4 or Q.")
            print("Please try again")
            menu()
            
        choice=input("""On which section would you like to continue ? 
1: Part 1 | 2: Part 2 | 3: Part 3 | 4: Part 4 | Q: Quit
                     """)


menu()
