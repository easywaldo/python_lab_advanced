from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request 

"""
ProcessPollExecutor
"""


URLS = [
    'http://www.daum.net',
    'http://www.naver.com',
    'http://www.yes24.com',
    'http://www.wconcept.co.kr'
]

TIMEOUT = 3

# 실행함수
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()
      

def main():
    # process pool context
    with ProcessPoolExecutor(max_workers=5) as executor:
        # Future load(not execute)
        future_to_url = {executor.submit(load_url, url, TIMEOUT): url for url in URLS}
        
        # print(future_to_url)
        
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            
            try:
                date = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(date)))

if __name__ == '__main__':
    main()