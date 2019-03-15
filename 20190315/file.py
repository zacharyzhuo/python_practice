# 讀取整個檔案
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 逐行讀取
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines() # 讀取檔案內容並存成串列

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# 寫入檔案
filename = 'programming.txt'

# open()函式第二個引數，共有三種分別為'r''w''a'，預設為'r'讀取
# 'w'為寫入的意思
with open(filename, 'w') as file_object: 
    file_object.write("I love programming.\n") # 需加入換行符號才會換行
    file_object.write("I am handsome.\n")

# 'a'附加在原本檔案後面
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    