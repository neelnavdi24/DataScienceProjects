# Loading the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset
df = pd.read_csv('cars.csv')
df.head()

#Checking the shape of the dataset
df.shape