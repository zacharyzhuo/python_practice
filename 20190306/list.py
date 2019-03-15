customers = ['zachary', 'rick', 'benny']
print("歡迎 " + customers[0] + " / " + customers[1] + " / " + customers[2] +" 的蒞臨")

print("哎呀!!" + customers[0] + "無法出席")
customers[0] = 'kenny'
print("歡迎 " + customers[0] + " / " + customers[1] + " / " + customers[2] +" 的蒞臨")

print('找到更大的餐桌了 欸嘿')
customers.insert(0 , 'tony')
customers.insert(2 , 'tim')
customers.append('amy')
print("歡迎 " + customers[0] + " / " + customers[1] + " / " + customers[2] + " / " +
customers[3] + " / " + customers[4] + " / " + customers[5] +" 的蒞臨")

print('餐桌沒了只有兩人能吃其他人 滾~')
getOut = customers.pop()
print(getOut + ' 滾')
getOut = customers.pop()
print(getOut + ' 滾')
getOut = customers.pop()
print(getOut + ' 滾')
getOut = customers.pop()
print(getOut + ' 滾')
print("剩下 " + customers[0] + " / " + customers[1] + "兩位")

print("騙你的 誰都沒東西吃 ㄏㄏ")
del customers[1]
del customers[0]
print("名單剩下 " + str(customers))