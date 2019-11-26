# A program to read data from a csv file with pandas and calculate the mean.

import time
import os
import pandas as pd

while True:
    if os.path.exists("temps.csv"):
        Data = pd.read_csv("temps.csv")
        Data.describe()
        print(Data.mean())
    else:
        print("File not found")
    time.sleep(10)


