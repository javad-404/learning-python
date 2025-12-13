def claculate_masahat(**kwargs):
    print (f"my kwargs is {kwargs}")
    if 'tool' in kwargs:
        return kwargs['tool'] * kwargs['ertefa']
    if 'shoa' in kwargs:
        return kwargs['shoa'] * 3.1415926 * kwargs['shoa']
    return 0
    
print(claculate_masahat(  tool = 9, ertefa = 3))