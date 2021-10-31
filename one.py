import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random
import pandas as pd 
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

populationMean=statistics.mean(data)
standeredDeviation=statistics.stdev(data)
print("mean =",populationMean)
print("standeredDeviation =",standeredDeviation)
fig = ff.create_distplot([data],["Math_score"],show_hist=False)

fig.show()





