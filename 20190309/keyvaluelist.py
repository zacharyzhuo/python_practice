# 字典串列
alien_0 = {'color': 'yellow', 'point': 5}
alien_1 = {'color': 'green', 'point': 15}
alien_2 = {'color': 'blue', 'point': 25}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 把串列放入字典
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print('You order a ' + pizza['crust'] + '-crust pizza ' +
    'with the following toppings:')

for topping in pizza['toppings']:
    print('\t' + topping)

# ex
favorite_language = {
    'zachary': ['javascript', 'golang', 'python'],
    'rick': ['golang'],
    'benny': ['javascript', 'java'],
    'kenny': ['java']
}

# 加入if判斷串列長度為1的時候
for name, languages in favorite_language.items():
    if len(languages) == 1:
            print('\n' + name.title() + 
            "'s favorite language is: " +
            str(languages[0]))
    else:
        print('\n' + name.title() + "'s favorite language are:")
        for language in favorite_language[name]:
            print('\t' + language)

# 字典中的字典
users = {
    'zachary': {
        'first': '育辰',
        'last' : '卓',
    },
    'rick': {
        'first': '哲禎',
        'last': '林',
    },
}

for username, user_info in users.items():
    print('\nUsername: ' + username.title())
    print('\tFull name: ' + 
    user_info['last'] + user_info['first'])