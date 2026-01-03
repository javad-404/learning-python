import pandas

data = pandas.read_csv("squirrel_data.csv")

gray_data = data[data["Primary Fur Color"] == "Gray"]
cinnamon_data = data[data["Primary Fur Color"] == "Cinnamon"]
black_data = data[data["Primary Fur Color"] == "Black"]

gray_count = len(gray_data)
cinnamon_count = len(cinnamon_data)
black_count = len(black_data)

new_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_count, cinnamon_count, black_count]
}
new_data = pandas.DataFrame(new_dict)
new_data.to_csv("squirrel_count.csv", index=False)
