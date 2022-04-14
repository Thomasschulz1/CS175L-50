import matplotlib.pyplot as plt
import numpy as np
def main():
     try:
        expense_file = open('expenses.txt','r')
     except IOError:
        print(' File not found')
def pie_chart(pi):
    expense_pie = []
    for x in pi:
        x =  n.strip('\n')
        expense_list.append(n.split('\t'))
    pie = []
    name = []
    for a in expense_pie:
        pie.append(a[1])
        name.append(a[0])
    y = np.array(pie)
    label = name 
    plt.pie(y, labels = label)         
    plt.show()
        
main()
 
