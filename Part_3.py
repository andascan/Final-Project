# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:38:32 2019

@author: andascan
"""

import xlrd
import numpy as np

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

def get_path_length(path):
    path = np.append(path,path[0])
    total_length = 0.0
    for i in range(len(path)-1):
        j = path[i]
        k = path[i+1]
        dist = distances[j, k]
        total_length += dist
    return total_length

""" Shortest Path """
path = [5]

for i in range(len(coordinates[:,0])-1):        
    dist_list = list(distances[path[-1]])
    for j in range(len(dist_list)):
        if dist_list.index(min(dist_list)) in path:
            dist_list.remove(min(dist_list))
    path.append(dist_list.index(min(dist_list)))
length_of_my_algorithm = get_path_length(path)

print('Length of my algorithm is: ' + str(length_of_my_algorithm) + ' km')

