import time
def lookup(index,keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
        
    return []

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1 



