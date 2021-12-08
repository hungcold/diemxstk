import matplotlib.pyplot as plt
import numpy as np

divisions = ["Div-a","Div-b","Div-c","Div-d","Div-e"]
divisions_averge_marks = [70,82,73,65,68]
boys_average_marks = [68,67,77,61,70]

index = np.arange(5)
width = 0.30

plt.bar(index,divisions_averge_marks,width,color='green', label = 'Division marks')
plt.bar(index+width,boys_average_marks,width,color = 'blue', label = 'boys marks', bottom=divisions_averge_marks)
plt.title("bar graph")
plt.title("horizontally stacked bả garaph")

plt.xlabel("divisions")
plt.ylabel("marks")
plt.xticks(index+ width/2,divisions)

plt.legend(loc = 'best')
plt.show()
