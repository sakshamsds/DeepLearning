# Self Organising Map 
# Fraud Detection

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv("Credit_Card_Applications.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0,1))
X = sc.fit_transform(X)

# Training the SOM
from minisom import MiniSom
som = MiniSom(x=10, y=10, input_len=15, sigma=1, learning_rate=0.5)
som.random_weights_init(X)
som.train_random(X, num_iteration=100)

# Visualizing the results
# Higher the Mean Inter-node Distance, implies more the outlier
from pylab import bone, pcolor, plot, show, colorbar
bone()
pcolor(som.distance_map().T)
colorbar()
markers = ['o', 's']
colors = ['r','g']
for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[0]+0.5,                      #putting marker in the center of winning node
         w[1]+0.5,
         markers[y[i]],
         markeredgecolor = colors[y[i]],
         markerfacecolor = 'None',
         markersize = 10,
         markeredgewidth = 2)
show()  

# Finding the frauds 
mappings = som.win_map(X)
frauds = np.concatenate((mappings[(5,2)], mappings[(7,3)]), axis = 0)
frauds = sc.inverse_transform(frauds)
