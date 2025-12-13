def zarb(*args):
    res = 1
    for i in args:
        res*= i
    return res
b = zarb(2,9,2,3,6,69,4,10)

print(b)
