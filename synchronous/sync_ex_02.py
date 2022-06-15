import requests
import time
import concurrent.futures
import threading

# 각 스레드에 생성이 되는 객체
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session

def request_site(url):
    # 세션 획득
    session = get_session()
    
    print(session)
    print(session.headers)
    
    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, Status Code : {response.status_code} from {url}]')

def request_all_sites(urls):
    # 멀티스레드 실행
    # 반드시 max_workers 갯수 조절 필요하다
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)
    
            

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
