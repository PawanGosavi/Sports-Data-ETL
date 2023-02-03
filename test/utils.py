# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:33:25 2023

@author: PGosavi
"""

import os
import pandas as pd
import numpy as np

def get_current_path():
    cur_dir = os.getcwd()
    path = cur_dir
    print(f"\nCurrent path = '{path}.'\n")
    return path

def create_path(directory):
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)
    print(f"\nPath = '{path}'.\n")
    return path

def open_path(directory):
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, directory)
    print(f"\nPath = '{path}'.\n")
    return path

def create_dir(path):
    if os.path.isdir(path):
        print(f"\nDirectory '{path}' already exists.\n")
    else:
        os.mkdir(path)
        print(f"\nDirectory '{path}' created.\n")
    return path

def get_filename(fname, path):
    file_name = os.path.join(path, str(fname) + '.csv')
    print(f"\nFilename = '{file_name}.'\n")
    return file_name

def read_csv_data(fname):
    df = pd.read_csv(fname, index_col = False)
    print("")
    print(df.head())
    print("")
    return df

def get_columns_list(dfname):
    collist = dfname.columns.tolist()
    print(f"\nColumns : {collist}\n")
    return collist

def get_row_count(dfname):
    print(f"\nRow Count : {dfname.shape[0]}\n")
    return dfname.shape[0]

def get_column_count(dfname):
    print(f"\nColumn Count : {dfname.shape[1]}\n")
    return dfname.shape[1]

def test_compare_data(src_data, tgt_data):
    if src_data == tgt_data:
        return "Passed"
    else:
        return "Failed"

def test_compare_df(src_df, tgt_df):
    if src_df.equals(tgt_df):
        return "Passed"
    else:
        return "Failed"

def create_file(df, file_name, path, indexing = False):
    if os.path.isfile(file_name):
        print(f"\nFile '{file_name}' already exists.\n")
        create_v = input("Want to Create file again? : 'y' or 'n' : ").lower()
        print("")
        if create_v == 'y':
            if os.path.isdir(path):
                return df.to_csv(file_name, header = True, index = indexing)
            else:
                print(f"\nDirectory '{path}' does not exists.\n")
        else:
            pass
    else:
        if os.path.isdir(path):
            print(f"\nFile '{file_name}' created.\n")
            return df.to_csv(file_name, header = True, index = indexing)
        else:
            print(f"\nFile can not be created, because directory '{path}' does not exists.\n")
    