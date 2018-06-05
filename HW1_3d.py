"""
Name: Lai Wei
Email: laiw12@bu.edu
"""
#!/usr/bin/python

import scipy
import scipy.io
import networkx as nx

import requests
import re
import matplotlib.pyplot as plt


response = requests.get('https://escience.rpi.edu/data/DA/fb100/')
html = response.text
tokens = re.split('>|<', html)
files = [token for token in tokens if token[-3:] == 'mat' and token != 'schools.mat']

#for f in files:
	#with open(f, 'wb') as handle:
	#	response = requests.get('https://escience.rpi.edu/data/DA/fb100/' + f, stream=True)

	#	if not response.ok:
		#	print('Download of ' + f + ' failed.')
#
	#	handle.write(response.content)

## construct

# load the .mat file into a dictionary (associative array) 
X = [0 for x in range(len(files))]
Y = [0 for y in range(len(files))]
Y1 =[0 for y in range(len(files))]
for f in range(1):
    d = {}
    scipy.io.loadmat(files[f], d)

#  of the .mat data, we only care about the adjacency matrix named A.
#  skip the other stuff and print only the contents of (value associated with key) A.
 
    for keys,values in d.items():
        if keys == "A":
            matrix = values
       
    G = nx.Graph(matrix)
    
## people's friends

    A =G.degree(G.nodes())
    
    
    giant = max(nx.connected_component_subgraphs(G), key=len)
    print(giant)
    size= giant.number_of_nodes()
    diameter = nx.diameter(giant)
    avg = nx.average_shortest_path_length(giant)
    print('component_size:',size)
    print('diameter：',diameter)
    print('avg shortest path:',avg)
    X[f] = size
    Y[f] =diameter
    Y1[f] = avg






fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax1.scatter(X,Y)
ax2.scatter(X,Y1)




########
# Each line of output will look like 
## (45, 5972)	1.0 
#
# Meaning an edge is present between student 45 and student 5972.
# We won't use the edge weight 1.0 -- feel free to improve this code and 
# use your Python skills to strip that out.

