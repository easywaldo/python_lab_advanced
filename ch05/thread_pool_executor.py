"""
Multithreading - Thread pool executor

concurrent.futures, xxxPoolExecutor

3.2 이상
with 사용으로 생성, 소멸 라이프사이클 관리 용이
디버깅 하기가 어렵다
대기중인 작업 -> Queue -> 완료 상태 조사 -> 결과 또는 예외 가 반환 -> 단일화(캡슐화)

"""

import logging
from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    logging.info('Sub Thread %s: starting', name)

    result = 0
    for i in range(10001):
        result = result + i
        
    logging.info('Sub THread %s: finishing result: %d', name, result)

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    logging.info("Main-Thread: before creating and running thread")
    
    # 실행방법1
    # max_worker : 작업의 개수가 넘어가면 직접,설정이 유리
    
    # executor = ThreadPoolExecutor(max_workers=3)
    # task1 = executor.submit(task, ('First',))
    # task2 = executor.submit(task, ('Second',))
    
    # 결과 값 있을 경우 출력
    # print(task1.result())
    # print(task2.result())
    
    
    
    # 실행방법 2
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ['First', 'Second', 'Third'])
        
        # 결과 확인
        print(list(tasks))
    
    
if __name__ == '__main__':
    main()
