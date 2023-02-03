# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 11:53:06 2023

@author: PGosavi
"""

import utils
import pandas as pd
import unittesting

test_case_id = 1

def testing ():
    
    global test_case_id
    
    # Source Data
    
    print("\n------------------ SRC Data ------------------\n")
    
    src_filename = "Extracted_Data"
    
    src_path = "extracted"
    
    src_fpath = utils.open_path(src_path)
    
    src_fname = utils.get_filename(src_filename, src_fpath)
    
    src_extracted_df = utils.read_csv_data(src_fname)
    
    temp_src_df = pd.DataFrame()
    
    temp_src_df['ID'] = src_extracted_df['ID'].astype('str').str.strip().fillna(0).astype('int')
    temp_src_df['Name'] = src_extracted_df['Name'].astype('str').str.strip().fillna("UNK").astype('str')
    temp_src_df['Age'] = src_extracted_df['Age'].astype('str').str.strip().fillna(0).astype('int')
    temp_src_df['Nationality'] = src_extracted_df['Nationality'].astype('str').str.strip().fillna("UNK").astype('str')
    temp_src_df['Joined'] = pd.to_datetime(src_extracted_df['Joined']).fillna(pd.to_datetime('2000-01-01')).astype('datetime64[ns]')
    temp_src_df['Weight_lbs'] = src_extracted_df['Weight'].astype('str').str.strip().str.rstrip('lbs').fillna(0).replace("nan", 0).astype('int')
    
    src_filt_df = temp_src_df[(temp_src_df['Age'] >= 18) & (temp_src_df['Nationality'] == "England") & (temp_src_df['Weight_lbs'] < 150)]
    
    src_ord_df = src_filt_df.sort_values(by=['Weight_lbs', 'Age'], ascending = False)
    
    src_df = src_ord_df
    
    src_r_count = utils.get_row_count(src_df)
    
    src_c_count = utils.get_column_count(src_df)
    
    src_collist = utils.get_columns_list(src_df)
    
    src_random_record = src_df[src_df['ID'] == 199960] 
    
    test_src_output = [{'SRC' : src_r_count},
                       {'SRC' : src_c_count},
                       {'SRC' : src_collist},
                       {'SRC' : src_random_record}]
    
    test_src_df = pd.DataFrame(test_src_output, index=['Row Count', 'Column Count', 'Column Names', 'Random Record'])
    
    # Target Data
    
    print("\n------------------ TGT Data ------------------\n")
    
    tgt_filename = "Loaded_Data"
    
    tgt_path = "loaded"
    
    tgt_fpath = utils.open_path(tgt_path)
    
    tgt_fname = utils.get_filename(tgt_filename, tgt_fpath)
    
    tgt_df = utils.read_csv_data(tgt_fname)
    
    tgt_r_count = utils.get_row_count(tgt_df)
    
    tgt_c_count = utils.get_column_count(tgt_df)
    
    tgt_collist = utils.get_columns_list(tgt_df)
    
    tgt_random_record = tgt_df[tgt_df['ID'] == 199960] 
    
    test_tgt_output = [{'TGT' : tgt_r_count},
                       {'TGT' : tgt_c_count},
                       {'TGT' : tgt_collist},
                       {'TGT' : tgt_random_record}]
    
    test_tgt_df = pd.DataFrame(test_tgt_output, index=['Row Count', 'Column Count', 'Column Names', 'Random Record'])
        
    # Testing

    print(f"\n------------------ Test Case ID : {test_case_id} ------------------\n")

    test_row_count = utils.test_compare_data(src_r_count, tgt_r_count)
        
    print(f"\nRow Count Check : {test_row_count}\n")
            
    test_col_count = utils.test_compare_data(src_c_count, tgt_c_count)
    
    print(f"\nColumn Count Check : {test_col_count}\n")
    
    test_col_names = utils.test_compare_data(src_collist, tgt_collist)
    
    print(f"\nColumn Names Check : {test_col_names}\n")
    
    test_random_record = utils.test_compare_df(src_random_record, tgt_random_record)
    
    print(f"\nRandom Record Check : {test_random_record}\n")
    
    test_case_output = [{'RESULT' : test_row_count},
                        {'RESULT' : test_col_count},
                        {'RESULT' : test_col_names},
                        {'RESULT' : test_random_record}]
    
    test_case_df = pd.DataFrame(test_case_output, index=['Row Count', 'Column Count', 'Column Names', 'Random Record'])
    
    test_output_df = pd.concat([test_src_df, test_tgt_df, test_case_df], axis = 1)
    
    # Output
    
    testing_df = test_output_df
    
    testing_path = utils.create_path("testing")
    
    testing_dir = utils.create_dir(testing_path)
    
    t_given_file_name = "Testing_Data"
    
    test_index = True
    
    t_file_name = utils.get_filename(t_given_file_name, testing_path)
    
    utils.create_file(testing_df, t_file_name, testing_path, test_index)

    return testing_df, src_df, tgt_df