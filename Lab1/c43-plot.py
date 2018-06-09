import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

# 1 .   Prepare data
labels = ["iOS","Android","Web","React Native"]
values = [20, 15, 40, 25]
colors = ["red","green","gold","purple"]
explode = [0,0,0,0.2]
# 2 .   Plot
pyplot.pie(values,
           labels=labels,
           colors = colors,
           explode=explode,
           shadow= True )
pyplot.axis("Equal")

# 3 .   Show
pyplot.show()