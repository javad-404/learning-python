import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
temp_average = data["temp"].mean()
max_temp = data["temp"].max()
describe = data.describe()

highest_temp = data[data.temp == data.temp.max()]
monday = data[data.day == "Monday"]
monday_temp = monday["temp"].item()
F = (monday_temp * 1.8) + 32
print(F)

rainy_days = data[data.condition == "Rain"]


