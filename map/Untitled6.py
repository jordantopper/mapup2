#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dataset = pd.read_csv(r'C:\Users\bikra\OneDrive\Desktop\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv')


# In[2]:


dataset


# In[3]:


def generate_car_matrix(dataset):
    # Your logic here
    # Ensure the returned DataFrame adheres to the given rules
    pass


# In[4]:


def generate_car_matrix(dataset):
    # Assuming 'id_1', 'id_2', and 'car' are column names in your dataset
    matrix = pd.pivot_table(dataset, values='car', index='id_1', columns='id_2', fill_value=0)
    matrix.values[[range(len(matrix))]*2] = 0  # Set diagonal values to 0
    return matrix


# In[5]:


result_matrix = generate_car_matrix(dataset)


# In[6]:


matrix.values[(range(len(matrix)), range(len(matrix)))] = 0  # Set diagonal values to 0


# In[7]:


# Step 1: Import necessary libraries
import pandas as pd

# Step 2: Load the dataset into a DataFrame
dataset = pd.read_csv(r'C:\Users\bikra\OneDrive\Desktop\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv')  # Replace 'path/to/your/dataset-1.csv' with the actual file path

# Step 3: Define the function to generate the car matrix
def generate_car_matrix(dataset):
    # Assuming 'id_1', 'id_2', and 'car' are column names in your dataset
    matrix = pd.pivot_table(dataset, values='car', index='id_1', columns='id_2', fill_value=0)
    matrix.values[(range(len(matrix)), range(len(matrix)))] = 0  # Set diagonal values to 0
    return matrix

# Step 4: Apply the function to the dataset
car_matrix = generate_car_matrix(dataset)

# Step 5: Display the resulting car matrix
car_matrix


# In[8]:


pip install pandas


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




