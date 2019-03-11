# while 迴圈
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 讓使用者決定什麼時候結束
prompt = '\nTell me something, and I will repeat it back to you: '
prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != "quit":
#         print(message)
# print("thank you")

# 旗標
active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#         # break
#     else:
#         print(message)

# continue 判斷
current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# while 迴圈使用在串列字典
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# while 迴圈使用 remove 刪除多個項目
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# ex
students = {}

active = True

while active:
    name = input('你叫啥? ')
    chinese = input('國文幾分? ')
    math = input('數學幾分? ')
    english = input('英文幾分? ')

    score = [int(chinese), int(math), int(english)]
    students[name] = score

    check = input('還要再問嗎? (y/n) ')

    if check.lower() == 'n':
        active = False

print("-----------公佈欄-----------")
print("姓名\t國文\t英文\t數學\t平均")

for name, scores in students.items():

    avg = (scores[0] + scores[1] + scores[2]) / 3

    print(name + "\t" + str(scores[0]) + "\t" + 
        str(scores[1]) + "\t" + str(scores[2]) + "\t" + str(avg))