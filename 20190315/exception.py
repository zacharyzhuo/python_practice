# 例外
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# try-except-else程式碼區塊
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        # pass 陳述句 讓程式什麼都不做
        print("You can't divide by zero!")
    else:
        print(answer)