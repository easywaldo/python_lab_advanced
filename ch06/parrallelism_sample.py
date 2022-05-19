"""
병렬성
    - 완전히 동일한 타이밍(시점)에 태스크 실행
    - 다양한 파트(부분)으로 나눠서 실행(합 나눠서 구하고 취합)
    - 멀티 프로세싱에서 CPU가 1Core인 경우 만족하지 않음.
    - 딥러닝, 비트코인, 채굴 등
    
Process vs Thread
    - 독립된 메모리(프로세스), 공유메모리(스레드)
    - 많은 메모리 필요(프로세스), 적은 메모리(스레드)
    - 좀비(데드)프로세서 생성 가능성, 좀비(데드) 스레드 생성 쉽지 않음
    - 오버헤드 큼(프로세스), 오버헤드 작음(스레드)
    - 생성/소멸 다소 느림(프로세스), 생성/소멸 빠름(스레드)
    - 코드 작성 쉬움/디버깅 어려움(프로세스), 코드 작성 어려움/디버깅 어려움(스레드)
"""


from multiprocessing import Process
import time
import logging

def proc_func(name):
    print('Sub-Process {}: starting'.format(name))
    time.sleep(3)
    print('Sub-Process {}: finishing'.format(name))
    
def main():
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # 함수인자확인
    p = Process(target=proc_func, args=('First',))
    
    logging.info('Main-Process: before creating Process')
    
    # 프로세스
    p.start()
    
    # logging.info('Main-Process: Terminated Process')
    # p.terminate()
    
    logging.info('Main-Process: During Process')
    p.join()
    
    
    # 프로세스 상태확인
    print(f'Process p is alive: {p.is_alive()}')
    

# 메인시작
if __name__ == '__main__':
    main()