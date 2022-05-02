# Ex1
# Use class

import time

class ExcuteTimer(object):
    def __init__(self, message):
        self._message = message
    
    def __enter__(self):
        self._start = time.monotonic()
        return self._start
    
    def __exit__(self, exc_type, exc_value, trace):
        if exc_type:
            print("Logging exception {}".format((exc_type, exc_value, trace)))
        else:
            print('{} : {} s'.format(self._message, time.monotonic() - self._start))
        return True
    
with ExcuteTimer('Start job') as t:
    print('Received start monotonic1 : {}'.format(t))
    # Excute job
    for i in range(0,1000000):
        pass
    raise Exception('Raise! Exception!!!') # 강제로 발생