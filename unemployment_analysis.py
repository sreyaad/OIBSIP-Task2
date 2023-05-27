# -*- coding: utf-8 -*-
"""Unemployment_Analysis"""

import pandas as pd
import numpy as np
import datetime

# for graphical visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df=pd.read_csv('/content/Unemployment in India.csv')

df.columns

df.shape
df.size

df.head()

df.dtypes

df[[' Estimated Unemployment Rate (%)',
                ' Estimated Employed',
                ' Estimated Labour Participation Rate (%)']].corr()

df.isnull().sum()

"""Drop Null Records"""

df.dropna(axis=0,inplace=True)

df.shape

df[df.duplicated()]

df.dtypes

df['Region'].value_counts()

sns.countplot(x=df['Region'],palette = "Set2")
plt.xticks(rotation='vertical')
plt.show()

df['Area'].value_counts()

sns.countplot(x=df['Area'],palette = "Set2")
plt.show()

px.scatter(data_frame=df, x=' Estimated Unemployment Rate (%)',
            y='Region',
            animation_frame=' Date')
