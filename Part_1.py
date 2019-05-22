# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:31:49 2019

@author: andascan
"""

import xlrd
import numpy as np
import matplotlib.pyplot as plt

""" Data Acquisitions System"""
def get_distance_matrix():
    workbook = xlrd.open_workbook('distancematrix.xls')
    worksheet = workbook.sheet_by_name("Sayfa1") # We need to read the data 
    #from the Excel sheet named "Sayfa1"
    num_rows = worksheet.nrows #Number of Rows
    num_cols = worksheet.ncols #Number of Columns
    
    result_data =[]
    for curr_row in range(3, num_rows):
        row_data = []
        for curr_col in range(2, num_cols):
            data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
            if type(data)==str:
                data = np.nan
            #print(data)
            row_data.append(data)
        result_data.append(np.array(row_data))
    return np.array(result_data)

def get_coordinates():
    workbook = xlrd.open_workbook('Coordinates.xlsx')
    worksheet = workbook.sheet_by_name("Sayfa1") # We need to read the data 
    #from the Excel sheet named "Sayfa1"
    num_rows = worksheet.nrows #Number of Rows
    num_cols = worksheet.ncols #Number of Columns
    
    result_data =[]
    for curr_row in range(1, num_rows):
        row_data = []
        for curr_col in range(2, num_cols):
            data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
            #print(data)
            row_data.append(data)
        result_data.append(np.array(row_data))
    return np.array(result_data)

""" Data """

distances = get_distance_matrix()
coordinates = get_coordinates()