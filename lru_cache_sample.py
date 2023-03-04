from functools import lru_cache

def fetch_user(user_id):
    print('loading db...')
    return {
        "userId": user_id,
        "email": f"{user_id}@email.com",
        "location": f"loc-{user_id}",
    }
    
@lru_cache(maxsize=2)
def get_user(user_id):
    return fetch_user(user_id)

from random import choice
if __name__ == '__main__':
    for i in range(10):
        get_user(user_id=choice(["alpha", "beta", "bravo"]))
    print(get_user.cache_info())
    