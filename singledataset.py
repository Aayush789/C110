import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import csv
import statistics
import pandas as pd

df = pd.read_csv("data.csv")
data = df["average"].tolist()

fig = ff.create_distplot([data],["average"], show_hist = False)

fig.show()

mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)
print("mean: ", mean)

print("standard_deviation: ",standard_deviation)

