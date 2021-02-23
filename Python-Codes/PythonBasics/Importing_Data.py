import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


## read csv file 
df_Data =pd.read_csv("pokemon_data.csv")

## read excel file 
##df_Data =pd.read_excel("pokemon_data.xlsx")

## read text file (tab \t separated)
#df_Data =pd.read_csv("pokemon_data.txt", delimiter = "\t")
# Note that in general we may separate columns using any delimiter

## read data file on a webpage
#import io
#import requests
#url="https://raw.githubusercontent.com/LukeAFullard/Data-Analysis-Codes/main/Python-Codes/PythonBasics/pokemon_data.csv"
#s=requests.get(url).content
#df_Data =pd.read_csv(io.StringIO(s.decode('utf-8')))







##  ---  Loading data graphically  ---  ###

### In Google colab, to load graphically
#from google.colab import files
#uploaded = files.upload()
#import io
#df_Data = pd.read_csv("pokemon_data.csv")



### In Python or Jupyter notebook to load graphically
# import tkinter as tk
# from tkinter.filedialog import askopenfilename
# import pandas as pd

# root = tk.Tk()
# root.withdraw() #Prevents the Tkinter window to come up
# csvpath = askopenfilename()
# root.destroy()
# print(csvpath)
# df_Data = pd.read_csv(csvpath)



print(df_Data.head(5))