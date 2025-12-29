import math

def paint_calc(height, width, cover):
    s = height * width
    number_of_can = s / cover
    number_of_can = math.ceil(number_of_can)
    print(f"you need {number_of_can} cans of paint")

test_h = 3   
test_w = 9   
coverage = 5 


paint_calc(height=test_h, width=test_w, cover=coverage)