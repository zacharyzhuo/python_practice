# 定義函式
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# 位置引數
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\n我有個 " + animal_type)
    print("我的 " + animal_type + " 的名字叫做 " + pet_name)

describe_pet('柴犬', '小巴')

# 關鍵字引數
describe_pet(animal_type='柴犬', pet_name='小巴')
describe_pet(pet_name='小巴', animal_type='柴犬')

# 預設值
def describe_pet2(pet_name, animal_type='狗'): # 預設值放後面
    """Display information about a pet."""
    print("\n我有個 " + animal_type)
    print("我的 " + animal_type + " 的名字叫做 " + pet_name)

describe_pet2(pet_name='小巴')

# 返回值
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

name = get_formatted_name('zachary', 'zhuo')
print(name)

# 返回字典
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

me = build_person('zachary', 'zhuo', 22)
print(me)

# 傳入串列
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['zachary', 'rick', 'benny']
greet_users(usernames)

# 傳入任意數量的引數到函式內
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni', 'green peppers')

# 使用任意數量的關鍵字引數
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
    location='princeton',filed='physics')

print(user_profile)