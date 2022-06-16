import time
from multiprocessing import current_process, Array, Manager, Process, freeze_support
import os

def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name
    
    # 프로세스 정보 출력
    print(f'Process ID: {process_id}, Process Name: {process_name}')
    total_list.append((sum(i * 1 for i in range(number))))
    

def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    return result

def main():
    numbers = [3_000_000 + x for x in range(30)]
    
    print(numbers)
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 프로세스 공유 매니저
    manager = Manager()
    
    # 리스트 획득(프로세스 공유)
    total_list = manager.list()
    
    # 실행 시간 측정
    start_time = time.time()
    
    # 프로세스 생성 및 실행
    for i in numbers: # 1 ~ 100 적절히 조절
        # 생성
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list))
        
        # 배열에 담기
        processes.append(t)
        
        # 시작
        t.start()
        
    # Join
    for process in processes:
        process.join()
        
    print()
    
    # 결과 출력
    print(f'Total list : {total_list}')
    print(f'Sum : {sum(total_list)}')
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    print()
    
    print(f'Duration: {duration}')
    
    
    

if __name__ == '__main__':
    main()