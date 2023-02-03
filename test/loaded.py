# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 18:03:47 2023

@author: PGosavi
"""

import utils
import transformed
import pandas as pd

def loaded_data():
    
    transformed_df = transformed.transformed_data()
    
    loaded_df = transformed_df
    
    loaded_path = utils.create_path("loaded")
    
    loaded_dir = utils.create_dir(loaded_path)
    
    l_given_file_name = "Loaded_Data"
    
    l_file_name = utils.get_filename(l_given_file_name, loaded_path)
    
    utils.create_file(loaded_df, l_file_name, loaded_path)
    
    return loaded_df