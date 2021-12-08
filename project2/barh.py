import matplotlib.pyplot as plt
import numpy as np

divisions = ["Div-a","Div-b","Div-c","Div-d","Div-e"]
divisions_averge_marks = [70,82,73,65,68]
variance = [5,8,7,6,4]
plt.barh(divisions,divisions_averge_marks,color='green')
plt.title("bar graph")
plt.xlabel("divisions")
plt.ylabel("marks")
plt.show()
