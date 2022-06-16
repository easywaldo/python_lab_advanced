"""
동시 프로그래밍 패러다임 변화
싱글 코어 >> 처리향상 미미, 저하 >> 비동기 프로그래밍 >> CPU연산, DB연동, API 호출대기 시간 늘어남 >> NonBlocking
"""

"""
파이선 3.4 >> 비동기(asyncio) 표준 라이브러리 등장
"""

import time
import asyncio

async def exe_calculate_sync(name, n):
    for i in range(1, n + 1):
        print(f'{name} ->>> {i} of {n} is calculating...')
        await asyncio.sleep(1)
    print(f'{name} - {n} workging done!!!')

async def process_sync():
    start = time.time()
    
    await asyncio.wait([
        exe_calculate_sync('One', 3),
        exe_calculate_sync('Two', 2),
        exe_calculate_sync('Three', 1)
    ])
    
    
    end = time.time()
    
    print(f'>>>> total seconds : {end - start}')
    
    
if __name__ == '__main__':
    # 파이썬 3.7 이상
    asyncio.run(process_sync())
    
    # 3.7 이하
    # asyncio.get_event_loop().run_until_complete(process_sync())
