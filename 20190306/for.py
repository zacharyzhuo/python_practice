pizzas = ['夏威夷', '章魚燒', '日式燒肉']
for pizza in pizzas:
    print('I love ' + pizza + ' pizza')
print('I really love pizza!\n')

#######################################################

numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# squares = [value**2 for value in range(1, 11)]

print('比大小')
print('max ' + str(max(squares)))
print('min ' + str(min(squares)))
print('sum ' + str(sum(squares)))

#######################################################

# ex1
for number in range(1, 21):
    print(number)

# ex2
odd_numbers = []
for odd_number in range(1, 21, 2):
    odd_numbers.append(odd_number)
print(odd_numbers)

# ex3
divisionThree = []
for x in range(3, 21, 3):
    divisionThree.append(x)
print(divisionThree)

# ex4
cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

# ex5
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# 複製串列
my_foods = ['apple', 'banana', 'guava']
friends_foods = my_foods[:]
print(my_foods)
print(friends_foods)

my_foods.append('pineapple')
friends_foods.append('icecream')
print(my_foods)
print(friends_foods)

# 4-10 ex
my_items = ['a', 'b', 'c', 'd', 'e']
print(my_items[:3])
print(my_items[2:4])
print(my_items[-3:])

# 4-11 ex
friends_pizzas = pizzas[:]
pizzas.append('巧克力')
friends_pizzas.append('泡菜')

for pizza in pizzas:
    print(pizza)
for firend_pizza in friends_pizzas:
    print(firend_pizza)