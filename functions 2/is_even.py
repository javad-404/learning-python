def is_even (n):
    return n % 2 == 0

def get_odds (nums):
    odds = []
    count = 0
    
    for i in nums :
        if not is_even(i):
            odds.append(i)
            count+=1
    return odds, count
my_nums = [ 1,3,6,5,8,7,9,10]

my_odd_lsit , count_odd = get_odds(my_nums)
print(my_odd_lsit,count_odd, sep= '+')
            
