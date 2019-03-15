# 使用者輸入 input

# if height >= 36:
#     print('\nyou are tall enough to ride!')
# else:
#     print('\nyou will be able to ride when you are a little older.')

number = input('輸入一個數字，讓我來判斷: ')
number = int(number)

if number % 2 == 0:
    print('肯定是偶數')
else:
    print('肯定是奇數')