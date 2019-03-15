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