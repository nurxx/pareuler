"""
Usage: opt1.py [options]

Options:
-p PRECISION --precision=PRECISION                  Set calculation precision
                                                    [default: 1000]
-t TASKS --tasks=TASKS                              Set number of tasks for paralel computing
                                                    [default: 4]
-o FILE --output=file                               Store result in a file
                                                    [default: result.txt]
-q --quiet                                          Hide program execution messages
                                                    [default: False]
"""

import concurrent.futures
import multiprocessing
from docopt import docopt
import sys, os
from decimal import *
import time
import math

results = []
def blockPrint():
    sys.stdout = open(os.devnull, 'w')



def partial_sum(start, end, prec, thread_id):
    print(f'Thread {thread_id}: Partial sum calculating from {start} to {end}')
    started = time.perf_counter()
    sum = 0
    getcontext().prec = prec
    for k in range(start,end):
        sum += Decimal(2*k +1)/math.factorial(2*k)
    ended = time.perf_counter()
    print(f'Thread {thread_id}: Finished in {round(ended-started,2)} secs')
    return sum
    
    
if __name__ == '__main__':
    args = docopt(__doc__)
    precision = int(args['--precision'])
    tasks = int(args['--tasks'])
    output_file = args['--output']
    quiet_mode = args['--quiet'] 
    getcontext().prec = precision
    start = time.perf_counter()
    if quiet_mode:
        blockPrint()
    print(f'Program info:\n\tPrecision:{precision}\n\tTasks running:{tasks}\n\tOutput file:{output_file}\n\tQuiet mode:{quiet_mode}')
    chunk_size = precision / tasks
    with multiprocessing.Pool(processes = tasks) as executor:
        data = executor.starmap(partial_sum,[(int(i*chunk_size), int((i+1)*chunk_size), precision, str(i + 1)) for i in range(tasks)])
            
    finish = time.perf_counter()
    euler_approximation = str(sum(data))
    print(euler_approximation)
    with open(output_file, "w") as f: 
        f.write(euler_approximation) 
    print(f'Finished in: {(finish-start)*1000} milliseconds')