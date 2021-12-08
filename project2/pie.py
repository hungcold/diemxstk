import matplotlib.pyplot as plt
import numpy as np

firms = ["firm a","firm b","firm c","firm d","firm e"]
market_share = [20,25,15,10,20]
Explode = [0,0.1,0,0,0]
plt.pie(market_share,explode=Explode,labels=firms,shadow=True,startangle=45)
plt.axis('equal')
plt.legend(title="list of firms")
plt.show()
