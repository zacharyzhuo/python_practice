# 使用JSON格式儲存資料
import json

number = [2, 3, 5, 7, 11, 13]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    #json.dump() 第一個是儲存的資料，第二個是儲存資料的檔案物件
    json.dump(number, f_obj)

# 讀取
filename = 'number.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(number)

# 重構範例
def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username)

greet_user()
    