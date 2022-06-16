import multiprocessing
import requests
import time
import concurrent.futures
import threading

# 각 프로세스 메모리 영역에 생성이 되는 객체 (독립적)
# 함수 실행 할 때마다 객체 생성은 좋지 않음. -> 각 프로세스마다 할당

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def request_site(url):
    # 세션 확인
    print(session)
    # print(session.headers)
    
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f'[{name} ->> Read Contents : {len(response.content)}, Status Code : {response.status_code} from {url}]')

def request_all_sites(urls):
    # 멀티프로세싱 실행
    # 반드시 max_processes 갯수 조절 후 session 객체 및 실행 시간 확인
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)
    
            

def main():
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org./dice",
        "https://realpython.com",
    ] * 3
    
    start_time = time.time()
    
    request_all_sites(urls)
    print()
       
    duration = time.time() - start_time
    print(f'Download {len(urls)} sites in {duration} seconds')
    
    
if __name__ == "__main__":
    main()
