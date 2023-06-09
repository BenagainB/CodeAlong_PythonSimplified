""" pandas_intro.py """
import pandas as pd
import sqlite3

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

# print(data)
#         name  height  weight         bmi
# 0     Mariya    1.67      54   19.362473
# 1     Batman    1.90     100   27.700831
# 2  Spongebob    0.25      10  160.000000

## Save dataframe to csv
# data.to_csv("bmi.csv", index=False)
# ,name,height,weight,bmi
# 0,Mariya,1.67,54,19.362472659471475
# 1,Batman,1.9,100,27.70083102493075
# 2,Spongebob,0.25,1,16.0

## comma delimited vs tab delimited
# data.to_csv("bmi.csv", index=False, sep="\t")  # can also save as "bmi.txt"
# name	height	weight	bmi
# 0	Mariya	1.67	54	19.362472659471475
# 1	Batman	1.9	100	27.70083102493075
# 2	Spongebob	0.25	1	16.0

## Load Data Frame from File
# data = pd.read_csv("bmi.csv")
# pd.read_csv("bmi.csv", sep="\t")
# print(data)

## Load SQL database to Data Frame
# connection = sqlite3.connect("gta.db")  # passing name of database
# gta_data = pd.read_sql("select * from gta", connection)    # gta is name of table, not database
# print(gta_data)

## Head and Tail Methods
# print(data.head())  # print first 5 rows, but could also pass variable number into head
# print(data.tail())  # print last 5 rows, but could also pass variable number into tail

## Filter Data Entries
# filtered_row = data[ data["name"] == "Batman" ]
# print(filtered_row)
#      name  height  weight        bmi
# 1  Batman     1.9     100  27.700831

## Replace Data Entries
# replaced_name = data.replace("Batman", "Superman")
# print(replaced_name)
#         name  height  weight        bmi
# 0     Mariya    1.67      54  19.362473
# 1   Superman    1.90     100  27.700831
# 2  Spongebob    0.25       1  16.000000

## Remove Columns
# remove_column = data.drop("bmi", axis=1)
# print(remove_column)
#         name  height  weight
# 0     Mariya    1.67      54
# 1     Batman    1.90     100
# 2  Spongebob    0.25       1

# remove_columns = data.drop(["weight", "bmi"], axis=1)
# print(remove_columns)
#         name  height
# 0     Mariya    1.67
# 1     Batman    1.90
# 2  Spongebob    0.25

remove_row = data.iloc[1:4] # omits 0 row, but keeps row 1-4
print(remove_row)

## Add New Rows to Data Frame
row = {"name": "Marvell",
       "height": 2.0,
       "weight": 110}
new_row_data = data.append(row, ignore_index = True)
print(new_row_data)

## Remove Duplicates
row = {"name": "Black Adam",
       "height": 2.0,
       "weight": 110}
new_row_data = new_row_data.append(row, ignore_index = True)
print(new_row_data)

scrubbed_data = new_row_data.drop_duplicates()  # removes exact duplicates
print(scrubbed_data)

scrubbed_data = new_row_data.drop_duplicates( subset = ["bmi"])
print(scrubbed_data)

print("number of entries:", len(scrubbed_data))
