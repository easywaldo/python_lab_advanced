"""
Sharing state
keyword - memory sharing, array, value
"""

from multiprocessing import Process, current_process, Value, Array
import os

# 프로세스 메모리 공유 예제(공유X)

# 실행함수
def generate_update_number(v: int):
    for _ in range(50):
        v.value += 1

    print(current_process().name, "data", v.value)
    

def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    
    # 출력
    print(f'Parent process Id {parent_process_id}')
    
    # 프로세스 리스트 선언
    process_list = list()
    
    # https://docs.python.org/3/library/multiprocessing.html
    # from multiprocessing import shared_memory
    # from multiprocessing import Manager 
    # process memory shared variable
    # share_numbers = Array('i', range(50))
    share_value = Value('i', 0)
    
    for _ in range(1, 10):
        # 생성
        p = Process(target=generate_update_number, args=(share_value,))
        
        process_list.append(p)
        
        p.start()
        
    for p in process_list:
        p.join()
        
    # 최종 프로세스 부모 변수
    print('Final Data in parent process', share_value.value)


if __name__ == "__main__":
    main()