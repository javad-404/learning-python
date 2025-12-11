def calculate_area (length, width):
    s = length * width
    return s
user_length = int(input('pls enter length: '))
user_width = int(input("pls enter width: "))
final_answer = calculate_area(user_length, user_width)
print(f"masahat is {final_answer}")
 