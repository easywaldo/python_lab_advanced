"""
프로세스
- 운영체제 >> 할당받는 지원 단위 (실행 중인 프로그램)
- CPU 동작 시간, 주소 공간 (독립적)
- Code, Data, Stack, Heap -> 독립적
- 최소 1개 의 메인 스레드 보유
- 파이프, 파일, 소켓 등을 사용해서 프로세스 간 통신(Cost 높음) -> Context Switching

스레드
- 프로세스 내에 실행 흐름 단위
- 프로세스 자원 사용
- Stack 만 별도 할당 , 나머지는 공유(Code, Data, Heap)
- 메모리 공유(변수 공유)
- 한 스레드의 결과가 다른 스레드의 영향 끼침
- 동기화 문제는 정말 주의(디버깅 어려움)

멀티스레드
- 한 개의 단일 어플리케이션(응용프로그램) -> 여러 스레드로 구성 후 작업 처리
- 시스템 자원 소모 감소(효율성), 처리량 증가(Cost 감소)
- 통신 부담 감소, 디버깅 어려움, 단일 프로세스에는 효과 미약, 자원 공유문제(교착상태) 발생 가능성, 프로세스 영향

멀티프로세스
- 한 개의 단일 어플리케이션(응용프로그램) -> 여러 프로세스로 구성 후 작업 처리
- 한 개의 프로세스 문제 발생은 확산 없음(프로세스 kill)
- 캐시 채인지, Cost 매우 높음(오버헤드), 복잡한 통신 방식 사용


keyword - Cpython, 메모리관리, GIL 사용 이유
Gil(Global Interpreter Lock)
    CPython -> Python(bytecode) 실행 시 여러 thread 사용할 경우
    한번에 하나의 스레드만 접근하여 작업을 할 수 있도록 제한을 걸 수 있도록 한다
        단일 스레드만이 Python object 에 접근하게 제한하는 mutex
        Cpython 메모리 괸리가 취약하기 때문 > Thread-safe
        단일스레드로도 충분히 빠르다
        프로세스 사용가능(Numpy/Scipy) 등 GIL 외부 영역에서 효율적인 코딩
        병렬처리는 multiprocessing, asyncio 선택지가 다양하다.
        thread 동시성 완벽 처리를 위해 -> Jython, IronPython, Stackless Python 등이 존재
"""

import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name):
    logging.info("Sub-Thread %s: starting", name)
    time.sleep(3)
    logging.info("Sub-Thread %s: finishing", name)

# 메인 영역
if __name__ == '__main__':
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")
    
    # 함수인지 확인
    x = threading.Thread(target=thread_func, args=('First',))
    
    logging.info("Main-Thread: before running thread")
    
    # 서브스레드 시작
    x.start()
    
    logging.info("Main-Thread: wait for the thread to finish")
    
    logging.info("Main-Thread: all done")
    

