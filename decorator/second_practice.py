import time


def time_to_run(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        
        duration = t2 - t1
        print(f"Execution took: {duration} seconds")
        
        return result
    return wrapper
  
        
@time_to_run  
def my_list(n):
    first_list = []
    for i in range(1, n+1):
        first_list.append(i)
    
    return first_list
    
    
if __name__ == "__main__":
    user_answer = int(input("pls enter the list size: "))
    result = my_list(user_answer)
    print(f"List created with length: {len(result)}")