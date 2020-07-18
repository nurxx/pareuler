"""
Usage: opt2.py [options]

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

import multiprocessing
import threading
from docopt import docopt
import sys, os
from decimal import *
import time
import math

results = []

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def partial_sum(start, end, step, prec, thread_id):
    global results
    print(f'Thread {thread_id}: Partial sum calculating from {start} to {end} with step {step}')
    start_thread = time.perf_counter()
    sum = 0
    getcontext().prec = prec
    for k in range(start, end, step):
        print(k)
        sum += Decimal(2*k + 1)/math.factorial(2*k)
            
    end_thread = time.perf_counter()
    print(f'Thread {thread_id}: Finished in {round(end_thread-start_thread,10)} secs')
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
    processes = []
    with multiprocessing.Pool(processes = tasks) as executor:
        data = executor.starmap(partial_sum,[(i, precision - tasks + i, tasks, precision, str(i+1)) for i in range(tasks)])    
    finish = time.perf_counter()
    euler_approximation = str(sum(data))
    print(euler_approximation)
    with open(output_file, "w") as f: 
        f.write(euler_approximation) 
    print(f'Finished in: {(finish-start)*1000} milliseconds')