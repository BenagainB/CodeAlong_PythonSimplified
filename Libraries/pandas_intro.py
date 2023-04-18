""" pandas_intro.py """
import pandas as pd

column = ["Mariya", "Batman", "Spongebob"]
# print(column)
# ['Mariya', 'Batman', 'Spongebob']

## Create a DataFrame
# data = pd.DataFrame(column)
# print(data)
#            0
# 0     Mariya
# 1     Batman
# 2  Spongebob

## Add a Column Name
# titled_column = {"name": column}
# data = pd.DataFrame(titled_column)
# print(data)
#         name
# 0     Mariya
# 1     Batman
# 2  Spongebob

## Add new Columns
titled_columns = {"name": column,
                  "height": [1.67, 1.9, 0.25],
                  "weight": [54, 100, 1]}

data = pd.DataFrame(titled_columns)
# print(data)
#         name  height  weight
# 0     Mariya    1.67      54
# 1     Batman    1.90     100
# 2  Spongebob    0.25      10

## Select Column in DataFrame
# select_column = data["weight"]
# print(select_column)
# 0     54
# 1    100
# 2     10
# Name: weight, dtype: int64

select_column = data["weight"][1]
# print(select_column)
# 100

## Select Row in DataFrame
# select_row = data.iloc[1]
# print(select_row)
# name      Batman
# height       1.9
# weight       100
# Name: 1, dtype: object

select_row = data.iloc[1]["weight"]
# print(select_row)
# 100

## Manipulate Data
bmi = []
# bmi (Body Mass Index) = weight/(height**2)
for i in range(len(data)):
    bmi_score = data["weight"][i]/(data["height"][i]**2)
    bmi.append(bmi_score)

data["bmi"] = bmi

print(data)
#         name  height  weight         bmi
# 0     Mariya    1.67      54   19.362473
# 1     Batman    1.90     100   27.700831
# 2  Spongebob    0.25      10  160.000000

## Save dataframe to csv
data.to_csv("bmi.csv")
