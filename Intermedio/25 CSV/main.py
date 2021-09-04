import pandas

table = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
groups = table.groupby(["Primary Fur Color"]).size()
groups = groups.rename({'Primary Fur Color': 'Fur Color', 0: 'Count'})
groups.to_csv("squirrels.csv")
