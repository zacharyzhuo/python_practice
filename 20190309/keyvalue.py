# key-value

# 新增
alien = {}
alien['color'] = 'green'
alien['point'] = 5
print(alien)

# 修改
alien['color'] = 'yellow'
print(alien)

# 刪除
del alien['point']
print(alien)

# for迴圈訪問字典
user = {
    'username': 'Zachary',
    'first': 'YUCHEN',
    'last': 'ZHUO'
}
for key, value in user.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

# 訪問字典中的鍵
favorite_languages = {
    'jan': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())

# 以特定順序訪問字典中的鍵
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    if name in friends:
        print('hi', name.title() + 
        ', I see you favorite language is ' +
        favorite_languages[name].title() + '!')

# 檢查該key是否有在字典中
if 'erin' not in favorite_languages.keys():
    print('Erin, please take out poll!')

# 訪問字典中所有值
for language in favorite_languages.values():
    print(language)

# 使用set讓value唯一不重複
for language in set(favorite_languages.values()):
    print(language)