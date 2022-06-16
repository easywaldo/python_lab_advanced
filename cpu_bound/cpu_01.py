import time

def cpu_bound(number):
    return sum(i * i for i in range(number))

def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    return result

def main():
    numbers = [3_000_000 + x for x in range(30)]
    
    print(numbers)
    
    # 실행 시간 측정
    start_time = time.time()
    
    # 실행
    total = find_sums(numbers)
    
    print()
    
    # 결과 출력
    print(f'Total list : {total}')
    print(f'Sum : {sum(total)}')
    

if __name__ == '__main__':
    main()