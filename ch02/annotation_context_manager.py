import contextlib
import time

# Ex1
# Use decorator

@contextlib.contextmanager
def my_file_writer(filename, method):
    f = open(filename, method)
    yield f # __enter__
    f.close() # __exit__
    
with my_file_writer('testfile4.txt', 'w') as f:
    f.write('Context manager Test4.\nContextlib Test4.')
    
    
# Ex2
# Use decorator timer

@contextlib.contextmanager
def ExcuteTimerDc(message):
    start = time.monotonic()
    try: # __enter__
        yield start
    except BaseException as e:
        print('Logging exception: {}: {}'.format(message, e))
        raise
    else: # __exit__
        print('{} : {}s'.format(message, time.monotonic() - start))

 
with ExcuteTimerDc('Start job') as t:
    print('Received start monotonic1 : {}'.format(t))
    # Excute job
    for i in range(0,1000000):
        pass
    raise ValueError('error occured..')