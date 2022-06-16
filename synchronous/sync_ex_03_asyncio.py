import multiprocessing
import aiohttp
import time
import asyncio


# pip3 install aiohttp
# I/O Bound asyncio

async def request_site(session, url):
    # 세션 확인
    print(session)
    print(session.headers)
    
    async with session.get(url) as response:
        print('Read Contents {0}, from {1}'.format(response.content_length, url))

async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        # 작업 목록
        tasks = []
        for url in urls:
            # 태스크 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)
        
        # task 확인
        print(*tasks)
        print(tasks)
        
        await asyncio.gather(*tasks, return_exceptions=True)    
            

def main():
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org./dice",
        "https://realpython.com",
    ] * 3
    
    start_time = time.time()
    
    # 파이썬 3.7 이상
    asyncio.run(request_all_sites(urls))
    
    # 3.7 이하
    # asyncio.get_event_loop().run_until_complete(request_all_sites(urls))
    
    
    
    print()
    
    # 실행시간 종료
    duration = time.time() - start_time
    print(f'Download {len(urls)} sites in {duration} seconds')
    
    
if __name__ == "__main__":
    main()
