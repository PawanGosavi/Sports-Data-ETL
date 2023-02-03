# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 17:35:47 2023

@author: PGosavi
"""

import unittest
import utils
import testing

class TestStringMethods(unittest.TestCase):
    
    def test_positive(self):
        
        testing_df, src_df, tgt_df = testing.testing()
        
        src_r_count = utils.get_row_count(src_df)
    
        src_c_count = utils.get_column_count(src_df)
    
        src_collist = utils.get_columns_list(src_df)
        
        tgt_r_count = utils.get_row_count(tgt_df)
    
        tgt_c_count = utils.get_column_count(tgt_df)
    
        tgt_collist = utils.get_columns_list(tgt_df)
        
        error_message = "SRC & TGT are not equal !"
        
        self.assertEqual(src_r_count, tgt_r_count, error_message)
        
        self.assertEqual(src_c_count, tgt_c_count, error_message)
        
        self.assertEqual(src_collist, tgt_collist, error_message)