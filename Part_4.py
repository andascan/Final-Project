# -*- coding: utf-8 -*-
"""
Created on Thu May 23 01:03:01 2019

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

""" Genetic Algorithm """

def get_path():
  n = len(coordinates[:,0])
  l = list(range(n))
  np.random.shuffle(l)
  l.remove(5)
  l = [5] + l
  return l

def get_path_length(path):
    path = np.append(path,path[0])
    total_length = 0.0
    for i in range(len(path)-1):
        j = path[i]
        k = path[i+1]
        dist = distances[j, k]
        total_length += dist
    return total_length

def draw_path(path):
  path_length = get_path_length(path)
  path = np.append(path,path[0])
  lat = coordinates[:, 0]
  lon = coordinates[:, 1]
  x = lon[path]
  y = lat[path]
  plt.plot(x,y,'-o')
  plt.title(str(path_length)+' km.', loc='center', fontsize=15)
  plt.axes().set_aspect('equal')

def cross_over(gene1,gene2, mutation=0.05):
  r = np.random.randint(len(gene1)) # cross over location
  newgene = np.append(gene1[:r],gene2[r:]) # may be a defunct gene
    
  missing = set(gene1)-set(newgene)
  elements, count = np.unique(newgene, return_counts=True)
  duplicates = elements[count==2]
  duplicate_indices=(newgene[:, None] == duplicates).argmax(axis=0)
  
  newgene[duplicate_indices]=list(missing) # now proper.
  
  if np.random.rand()<mutation:
    i1,i2 = np.random.randint(0,len(newgene),2)
    newgene[[i1,i2]] = newgene[[i2,i1]] 
  return newgene

def create_initial_population(m):
  population = []
  fitness = []
  for i in range(m):
    gene = get_path()
    path_length = get_path_length(gene)
    
    population.append(gene)
    fitness.append(path_length)
  
  population = np.array(population)
  fitness = np.array(fitness)  
  sortedindex = np.argsort(fitness)
  return population[sortedindex], fitness[sortedindex]

def next_generation(population):
  pop = []
  fit = []
  f=int(np.sqrt(len(population)))
  for gene1 in population[:f]:
    for gene2 in population[:f]:   
      x =  cross_over(gene1,gene2,mutation=0.05)
      l = get_path_length(x)
      pop.append(x)
      fit.append(l)
  
  population = np.array(pop)
  fitness = np.array(fit)  
  sortedindex = np.argsort(fitness)
  return population[sortedindex], fitness[sortedindex]

generation_size = 3000
n_population=1000
population, fitness  = create_initial_population(n_population)

for i in range(generation_size):
    population, fitness = next_generation(population)
    if i%5 == 0:
        print(i)

shortest_path = list(population[0])
draw_path(shortest_path)

    
    







