def is_even (n):
    return (n % 2 ==0)
def any_even_is_true (nums):
    for n in nums:
        if is_even(n):
           return True
    return False
my_list =[1 , 5, 7,6]
print(any_even_is_true(my_list))
