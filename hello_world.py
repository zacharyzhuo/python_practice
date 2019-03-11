# by Zachary 2019/3/5
# 什麼我很帥

# str = "hello world"
# print(5 + 3)
# print(4 * 2)
# print(2 ** 3)
# print(16 / 2)

friends = ['zachary', 'kenny', 'rick', 'benny']

print(friends)
print(friends[0].title() + " is the most handsome!")

# append() 增加項目
friends.append('eric') 
print(friends)

# del() 刪除後不再使用此項目
del friends[1] 
print(friends)

# pop() 刪除後還會用到此項目
new_firends = friends.pop()
print(new_firends)
print(friends)

new_firends = friends.pop(1)
print(new_firends)
print(friends)

# remove() 刪除指定項目

friends.remove('zachary')
print(friends)