"""
Python Event 객체
1. Flag 초기값(0)
2. Set() -> 1. Clear -> 0. Wait(1 -> 리턴, 0 -> 대기), isSet() -> 현 플래그 상태

"""


import concurrent.futures
import logging
import queue
import random
import threading
import time

def producer(queue, event):
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info('Producer got message: %s', message)
        queue.put(message)
        
    logging.info('Producer received event Exiting')
        

def consumer(queue, event):
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info('Consumer storing message: %s (size=%d)', message, queue.qsize())
        
    logging.info('Consumer received event Exiting')
    

if __name__ == "__main__":
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # 사이즈 중요
    pipeline = queue.Queue(maxsize=10)
    
    # 이벤트 플래그 초기값 0
    event = threading.Event()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        
        # 실행시간 조정
        time.sleep(1)
        
        logging.info('Main : about to set event')
        
        # 프로그램 종료
        event.set()
        