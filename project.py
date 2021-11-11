import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import pandas as pd
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()


def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)

stdev_sd = statistics.stdev(mean_list)
mean_sd = statistics.mean(mean_list)
print("Mean of Sample dist is ",mean_sd)
print("Stdv of sample dist is ",stdev_sd)

stdv1_start,stdv1_end = mean_sd-stdev_sd,mean_sd+stdev_sd
stdv2_start,stdv2_end = mean_sd-(2*stdev_sd),mean_sd+(2*stdev_sd)
stdv3_start,stdv3_end = mean_sd-(3*stdev_sd),mean_sd+(3*stdev_sd)





fig = ff.create_distplot([mean_list],["Claps"],show_hist = False)
fig.add_trace(go.Scatter(
    x = [mean_sd,mean_sd],
    y = [0,0.17],
    mode = "lines",
    name = "mean"
))
fig.add_trace(go.Scatter(
    x = [stdv1_start,stdv1_start],
    y = [0,0.17],
    mode = "lines",
    name = "stdv1_start"
))
fig.add_trace(go.Scatter(
    x = [stdv1_end,stdv1_end],
    y = [0,0.17],
    mode = "lines",
    name = "stdv1_end"
))
fig.add_trace(go.Scatter(
    x = [stdv2_start,stdv2_start],
    y = [0,0.17],
    mode = "lines",
    name = "stdv2_start"
))
fig.add_trace(go.Scatter(
    x = [stdv2_end,stdv2_end],
    y = [0,0.17],
    mode = "lines",
    name = "stdv2_end"
))
fig.add_trace(go.Scatter(
    x = [stdv3_end,stdv3_end],
    y = [0,0.17],
    mode = "lines",
    name = "stdv3_end"
))

df1 = pd.read_csv("medium_data.csv")
data1 = df1["claps"].tolist()
mean_of_sample1 = statistics.mean(data1)
print("Mean of sample1 is ",mean_of_sample1)
fig.add_trace(go.Scatter(
    x = [mean_of_sample1,mean_of_sample1],
    y = [0,0.17],
    mode = "lines",
    name = "mean_of_sample1"
))

fig.show()

zScore = (mean_sd-mean_of_sample1)/stdev_sd

print("zScore is ",zScore)
