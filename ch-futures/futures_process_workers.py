from concurrent import futures
import multiprocessing
import random

def compute():
    return sum(
        [random.randint(1, 100) for i in range(1000000)]
    )

# concurrent.futures 가 multiprocessing.cpu_count를 호출하여 워커수를 결정한다

print("cpu count %d" % multiprocessing.cpu_count())

with futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(compute) for _ in range(8)]
    
results = [f.result(timeout=1000) for f in futures]

print("Results: %s" % results)