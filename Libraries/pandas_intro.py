import pandas as pd

column = ["Mariya", "Batman", "Spongebob"]
# print(column)
# ['Mariya', 'Batman', 'Spongebob']

# data = pd.DataFrame(column)
# print(data)
#            0
# 0     Mariya
# 1     Batman
# 2  Spongebob

titled_column = {"name": column}
data = pd.DataFrame(titled_column)
print(data)
#         name
# 0     Mariya
# 1     Batman
# 2  Spongebob

