import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import csv
import statistics
import pandas as pd

df = pd.read_csv("data.csv")
data = df["average"].tolist()

# code to find the mean of 100 data points 1000 and pllot it.
# function to get the mean of the given data samples.

def random_set_of_mean(counter):
    dataSet = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
#funtion to plot the mean of the graph

 def show_fig(mean_list):
     df = mean_list
     mean = statistics.mean(df)

     fig = ff.create_distplot([data],["average"], show_hist = False)
     fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list) 

    mean = statistics.mean(mean_list)
    print("mean of the sampling distribution: ",mean)
setup()

population_mean = statistics.mean(data)
print("population mean: ", population_mean)

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)

    std_devaition = statistics.mean(mean_list)
    print("std deviation of the sampling distribution: ", std_devaition)

standard_deviation()









 
