import time

def start_end(func):
    
    def wrapper(*args):
        print('starting')
        start = time.time()
        result = func(*args)
        end = time.time() - start
        print('finished')
        print("Time taken:", end)
        return result
    
    return wrapper

@start_end
def summ(a, b):
    print(a + b)

@start_end
def mul(a,b):
    time.sleep(2)
    print(a*b)

summ(5, 4)
mul(3, 4)