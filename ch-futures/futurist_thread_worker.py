import futurist
from futurist import waiters, rejection
import random

def compute():
    return sum(
        [random.randint(1, 100) for _ in range(100000)]
    )
    
with futurist.ThreadPoolExecutor(max_workers=8,
                                 check_and_reject=rejection.reject_when_reached(2)) as executor:
    futures = [executor.submit(compute) for _ in range(8)]
    print(executor.statistics)
    
results = waiters.wait_for_all(futures)
print(executor.statistics)

print("Results: %s" % [r.result() for r in results.done])
