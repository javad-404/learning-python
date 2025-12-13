def find_expensive(**kwargs):
    final_list = []
    gerani = 1000
    for name, price in kwargs.items():
        if gerani < price:
            final_list.append(name)
    return final_list
          

result = find_expensive(laptop=50000, gum=500, book=2500)
print(result)