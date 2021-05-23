import matplotlib.pyplot as plt
day = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
dataReddit = [0.5,0.2,0.3,-0.1,-0.4,0.3,0.7]
datatwitter = [0.4,0.3,0.4,-0.2,-0.5,0.1,0.5]
lineReddit = plt.plot(day, dataReddit, color='#FF4500')
lineTwitter = plt.plot(day, datatwitter, color='#1da1f2')
plt.xlabel('Day',color="green")
plt.ylabel('Sentiment',color="green")
plt.title('Sentiment Reddit/Twitter')
plt.legend(['Reddit', 'Twitter'], loc=3)
plt.axhline(y=0, color='black', linestyle='-')
plt.grid(True)
plt.show()

