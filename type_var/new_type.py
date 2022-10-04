from typing import NewType, Optional

UserId = NewType('UserId', int)
some_id = UserId(100)

def get_user_name(user_id: UserId) -> Optional[str]:
    user_list = {
        100: "easywaldo",
        200: "alpha",
        300: "bravo"
    }
    user = user_list[user_id]
    if user:
        return user
    else:
        return None

user_a = get_user_name(UserId(100))
print(user_a)
# user_b = get_user_name(UserId(-200))
# print(user_b)

output = UserId(23413) + UserId(54341)
print(output)