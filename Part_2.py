# -*- coding: utf-8 -*-
"""
Created on Wed May 22 13:37:21 2019

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

""" Random Path """

random_path = list(range(len(coordinates)))
random_path.remove(5)
np.random.shuffle(random_path)
random_path = [5] + random_path

def get_path_length(path):
    path = np.append(path,path[0])
    total_length = 0.0
    for i in range(len(path)-1):
        j = path[i]
        k = path[i+1]
        dist = distances[j, k]
        total_length += dist
    return total_length

length_random_path = get_path_length(random_path)

# Plot random path:
x = coordinates[random_path, 1]
y = coordinates[random_path, 0]

plt.title('Length of random path: ' + str(length_random_path) + ' km')
plt.plot(x, y, '-r')
plt.ylim(36, 43), plt.xlim(25, 45)
plt.axes().set_aspect('equal')
plt.show()
