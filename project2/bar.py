import matplotlib.pyplot as plt
import numpy as np

divisions = ["Div-a","Div-b","Div-c","Div-d","Div-e"]
divisions_averge_marks = [70,82,73,65,68]
plt.bar(divisions,divisions_averge_marks,color='green')
plt.title("bar graph")
plt.xlabel("divisions")
plt.ylabel("marks")
plt.show()
