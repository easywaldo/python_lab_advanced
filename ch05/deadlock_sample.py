"""
세마포어 : 프로세스간 공유 된 자원에 접근 시 문제 발생 가능성
-> 한개의 프로세스만 접근 처리 고안(경쟁상태 예방)

뮤텍스 : 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것. -> 경쟁 상태 예방

Lock : 상호 배제를 위한 잠금처리 -> 데이터 레이스 컨디션 방지
DeadLock : 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착상태)
Thread syncronization (스레드 동기화), 동기화 메서드 , 동기화 블럭
세마포어 와 뮤텍스 의 차이점?

    세마포어는 뮤텍스가 될 수 있지만
    뮤텍스는 세마포어가 될 수 없다.
    
    경쟁상태를 예방하기 위한 동기화 작업 메카니즘
    
    뮤텍스 게체는 단일 스레드가 리소스 또는 중요 섹션을 소비 허용
    세마포어는 리소스에 대한 제한된 수의 동시 엑세스를 허용

"""
import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class FakeDataStore:
    # 공유 변수
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
        
    def update(self, n):
        logging.info('Thread %s: starting update', n)
        
        # mutext & lock 등 동기화 필요한 부분(Thread syncronization)
        # lock 획득(방법1)
        # self._lock.acquire()
        # logging.info('Thread %s has lock', n)
        
        # local_copy = self.value
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy
        
        # # lock 반환
        # self._lock.release()
        
        
        # lock 획득(방법2)
        with self._lock:
            logging.info('Thread %s has lock', n)        
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

        
        logging.info('Thread %s: finishing update', n)

    


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    store = FakeDataStore()
    
    logging.info('Testing update. Starting value is %d', store.value)
    
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First', 'Second', 'Third', 'Forth']:
            executor.submit(store.update, n)
            
    logging.info('Testing update. Ending value is %d', store.value)