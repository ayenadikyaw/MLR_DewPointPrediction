# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 00:18:03 2019

@author: DELL
"""

import pandas as pd
import seaborn as sns
import matplotlib.pylot as plt
import numpy as np

df=pd.read_csv("TestData.csv")

sns.pairplot(df)

sns.heatmap(df.corr(),linewidth=0.2,vmax=1.0,square=True,linecolor="red",annot=True)