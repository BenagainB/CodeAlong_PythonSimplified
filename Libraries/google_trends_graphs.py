# google_trends_graphs.py
""" Plotting Google Trends Graphs with Matplotlib & Pandas """

import matplotlib.pyplot as plt
# import pytrends
from pytrends.request import TrendReq
import pandas as pd

# create a pytrends object. request data from Google Trends
pytrends = TrendReq(hl = 'en-US')   # hl is host language

# extract data about keywords
keywords = ['Python', 'R', 'C++', 'Java', 'HTML']   # limited to 5 keywords at a time
pytrends.build_payload(keywords, timeframe='today 5-y')
    # 5-y is the last 5 years, also is default value

# specify and get data
data = pytrends.interest_over_time()
    # represents weekly data regarding number of searches for each keyword
# print(data)
#             Python   R  C++  Java  HTML  isPartial
# date
# 2018-04-22      22  57   74    28    14      False
# 2018-04-29      20  55   74    23    13      False
# 2018-05-06      20  55   77    27    14      False
# 2018-05-13      20  54   75    29    15      False
# 2018-05-20      20  53   74    26    15      False
# ...            ...  ..  ...   ...   ...        ...
# 2023-03-19      34  50   89    23    15      False
# 2023-03-26      34  52   90    22    14      False
# 2023-04-02      31  47   89    21    13      False
# 2023-04-09      30  47   87    20    13      False
# 2023-04-16      32  47   89    22    13       True

# [261 rows x 6 columns]

# print(type(data))
# <class 'pandas.core.frame.DataFrame'>

# plot data
# plt.plot(data)

# add titles
# plt.suptitle('Programming Language Searches on Google')
# plt.xlabel('years')
# plt.ylabel('weekly searches')

# add legend
# plt.legend(keywords, loc='upper left')

# save graph
# plt.savefig('google_trends_graph.png')

# plt.show()

# analyze data
# focus = ['Python', 'Java'] # refine search to 2 keywords

# plt.plot(data[focus])
# plt.legend(focus)
# plt.savefig('google_trends_Python_vs_Java.png')
plt.show()

# extract country-level data about the keywords
data2 = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True)

# get countries with the most searches of 'Python' over the years
data2 = data2['Python'].nlargest(10)
# print(data2)
# geoName
# China          50
# Eritrea        44
# Israel         41
# St. Helena     32
# Russia         28
# Singapore      28
# South Korea    28
# Kyrgyzstan     26
# Armenia        24
# Hong Kong      24
# Name: Python, dtype: int64

# print(type(data2))
# <class 'pandas.core.series.Series'>

# convert to dataframe
data2 = data2.to_frame()
# print(data2)
#              Python
# geoName            
# China            50
# Eritrea          44
# Israel           41
# St. Helena       32
# Russia           28
# Singapore        28
# South Korea      28
# Kyrgyzstan       26
# Armenia          24
# Hong Kong        24

# print(type(data2))
# <class 'pandas.core.frame.DataFrame'>

# plot bar chart with PANDAS
# data2.plot(kind='bar')
# plt.show()

#plot a bar chart with multiple keywords
data3 = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True)
data3 = data3[55:60]
data3.plot(kind='bar')
plt.show()
