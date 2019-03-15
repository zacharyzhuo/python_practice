# if
my_age = 22
sister_age = 25

if my_age >= 22 and sister_age >= 25:
    print('yes')
else:
    print('no')
if my_age >= 22 or sister_age >= 25:
    print('yes')
else:
    print('no')

# 判斷特定值是否在串列之中
items = ['a', 'b', 'c']
result = 'a' in items
print(result)

# not in 關鍵字
users = ['zachary', 'rick', 'benny', 'kenny']
user = 'eric'
if user not in users:
    print(user.title() + ' get out of here')

# if-elif-else
if 'zachary' in users:
    print('yes')
elif 'rick' in users:
    print('yew')
else:
    print('none')

# 5-8 ex
users = ['admin', 'zachary', 'rick', 'benny', 'kenny']
# users = []
login = 'admin' # admin, zachary, eric
if users:
    if login in users and login =='admin':
        print('hello admin, would you like to see a status report?')
    elif login in users and login != 'admin':
        print('hello ' + login + ', thank you for logging in again.')
    else:
        print('get out!')
else:
    print('We need to find some users!')

# 5-10 ex
current_users = ['zachary', 'rick', 'benny', 'kenny', 'tom']
new_users = ['ZACHARY', 'rick', 'wan', 'lee', 'chen']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + ' 已被使用')
    else:
        print(new_user + ' 可使用')

# 5-11 ex
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    else:
        print(str(number) + 'rd')