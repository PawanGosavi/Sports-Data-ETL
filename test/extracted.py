# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:51:12 2023

@author: PGosavi
"""

import utils

def extracted_data():
    
    filename = "fifa_eda_stats"
    
    fpath = utils.get_current_path()
    
    fname = utils.get_filename(filename, fpath)
    
    raw_df = utils.read_csv_data(fname)
    
    # r_count = utils.get_row_count(raw_df)
    
    # c_count = utils.get_column_count(raw_df)
    
    collist = utils.get_columns_list(raw_df)
    
    desired_col_list = ['ID', 'Name', 'Age', 'Nationality', 'Joined', 'Weight']
    
    extracted_df = raw_df[desired_col_list]
    
    extracted_path = utils.create_path("extracted")
    
    extracted_dir = utils.create_dir(extracted_path)
    
    e_given_file_name = "Extracted_Data"
    
    e_file_name = utils.get_filename(e_given_file_name, extracted_path)
    
    utils.create_file(extracted_df, e_file_name, extracted_path)
    
    return extracted_df
