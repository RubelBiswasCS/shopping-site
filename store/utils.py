import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
# from random import random, randint
import random
# Pie Chart
def draw_piechart(products):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    # labels = 'Sale', 'Purchase', 'Test'
   
    labels = []
    
    for i in products:
        if i.category not in labels:
            labels.append(i.category)
    
    sizes = [random.randint(10,30), random.randint(30,50)]
    # explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = None
    fig1, ax1 = plt.subplots(1)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig1.savefig('media/piechart.png',dpi=100, transparent=True)
    
    

def draw_barchart():
    
   
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 35, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]
    men_std = [2, 3, 4, 1, 2]
    women_std = [3, 5, 2, 3, 3]
    width = 0.35       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, men_means, width, yerr=men_std, label='Men')
    ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
        label='Women')

    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.legend()

    fig.savefig('media/barchart.png',dpi=100, transparent=True)

    

