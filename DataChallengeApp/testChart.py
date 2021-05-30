# plot_time_series.py

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random
plt.style.use('seaborn')

dates = []
print(4*24)
date = datetime(2021, 5, 10, 0, 0, 0)
for i in range(365):
    for time in range(96):
        dates.append(date)
        date = date+timedelta(minutes=15)


y = []
num = random.randint(30000,40000)
for i in range(96*365):
    if random.randint(0,1):
        num += 20
    else:
        num -= 20
    y.append(num)


#y = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6]


#plt.tight_layout()
#plt.grid(True)
#plt.show()



lineReddit = plt.plot(dates, y, color='#FF4500')
plt.xlabel('Day',color="green")
plt.ylabel('Sentiment',color="green")
plt.title('Sentiment Reddit/Twitter')
plt.legend(['Reddit'], loc=3)
plt.axhline(y=20000, color='black', linestyle='-')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()