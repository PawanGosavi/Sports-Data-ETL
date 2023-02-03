# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 18:58:00 2023

@author: PGosavi
"""

from unittesting import TestStringMethods
import unittest

def main ():
    
    print("\n------------------ Operation Start ------------------\n")
    
    import utils

    import loaded
    
    loaded.loaded_data()
    
    import testing
    
    # testing.testing()  
    
    unittest.main()

    print("\n------------------ Operation End ------------------\n")

if __name__ == '__main__':
    main()
    