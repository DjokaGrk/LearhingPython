# with open("./Text_files/weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
# import csv

# with open("./Text_files/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#       if row[1] != "temp":
#         temperatures.append(int(row[1]))
#     print(temperatures)
import pandas

data = pandas.read_csv("./Text_files/weather_data.csv")
print(data["temp"])
