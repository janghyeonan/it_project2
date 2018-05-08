#!/usr/bin/env python3
# -*- coding: utf-8 -*-


### 저장 ###
from pandas import Series,DataFrame    
x_data = DataFrame(x)
y_data = DataFrame(y)

x_data.to_csv("/Users/hbk/github/it_project2/TH/x_data.csv",mode = "w")
y_data.to_csv("/Users/hbk/github/it_project2/TH/y_data.csv",mode = "w")


### 다운 ###
import pandas as pd

x_var = pd.read_csv("/Users/hbk/github/it_project2/TH/x_data.csv", index_col = 0).values
y_var = pd.read_csv("/Users/hbk/github/it_project2/TH/y_data.csv", index_col = 0).values

