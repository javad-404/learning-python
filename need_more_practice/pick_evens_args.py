def pick_evens(*args):
    my_even_list=[]
    for i in args:
        if i % 2 == 0:
            my_even_list.append(i)
    return my_even_list
print(pick_evens(11,3,12,94,9,5))