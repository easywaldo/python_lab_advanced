import requests
import time

def request_site(url, session):
    print(session)
    print(session.headers)
    
    with session.get(url) as response:
        print(f'[Read contents: {len(response.content)}, Status code : {response.status_code}] from {url}')

def request_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            request_site(url, session)
            

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
