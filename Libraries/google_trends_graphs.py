# google_trends_graphs.py
""" Plotting Google Trends Graphs with Matplotlib & Pandas """

import matplotlib
# import pytrends
from pytrends.request import TrendReq

# create a pytrends object. request data from Google Trends
pytrends = TrendReq(hl = 'en-US')   # hl is host language

# extract data about keywords
keywords = ['Python', 'R', 'C++', 'Java', 'HTML']   # limited to 5 keywords at a time
pytrends.build_payload(keywords, timeframe='today 5-y')
    # 5-y is the last 5 years, also is default value

# specify and get data
data = pytrends.interest_over_time()
    # represents weekly data regarding number of searches for each keyword
print(data)
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
