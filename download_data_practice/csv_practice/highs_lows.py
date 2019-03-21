import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get date, high, and low temperatures from file.
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], [] # 建立三個空串列
    for row in reader:
        try:
            # 將日期資料轉換為datetime物件
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            dates.append(current_date)

            high = int(row[1])
            highs.append(high)

            low = int(row[3])
            lows.append(low)
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5) # alpha 為透明度(0代表完全透明，1為預設表示不透明)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
tittle = "Daily high and low temperatures, - 2014\nDeath Valley, CA"
plt.xlabel(tittle, fontsize=20)
# 將日期斜放避免重疊
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

"""
%A 星期 如星期一
%B 月份 如一月
%m 以數字表示的月份 如01到12
%d 以數字表示月份中幾號 如03到31
%Y 四位數的年份 如2017
%y 兩位數的年份 如17
%H 24小時制的時數 如00到23
%I 12小時制的時數 如1到12
%p am或pm
%M 分鐘數 如00到59
%S 秒數 如00到61
"""