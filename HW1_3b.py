# -*- coding: utf-8 -*-
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
import math
import matplotlib.pyplot as plt
import operator


G = nx.Graph()
G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

G.add_edge(1,6)
G.add_edge(1,7)
G.add_edge(1,2)
G.add_edge(2,7)
G.add_edge(2,3)
G.add_edge(3,9)
G.add_edge(4,9)
G.add_edge(6,7)
G.add_edge(6,14)
G.add_edge(7,8)
G.add_edge(8,12)
G.add_edge(8,9)
G.add_edge(9,15)
G.add_edge(9,10)
G.add_edge(9,12)
G.add_edge(10,11)
G.add_edge(12,14)
G.add_edge(13,14)
G.add_edge(14,15)
G.add_edge(15,16)

##print(nx.degree_centrality(G))
##print(nx.closeness_centrality(G,normalized=False))
##print(nx.betweenness_centrality(G,normalized=False))
##print(nx.eigenvector_centrality(G))
##print(nx.pagerank(G))
#a=nx.degree_centrality(G)
#sorted_x = sorted(a.items(), key=operator.itemgetter(1))
#print(sorted_x)
     

########
# Each line of output will look like 
## (45, 5972)	1.0 
#
# Meaning an edge is present between student 45 and student 5972.
# We won't use the edge weight 1.0 -- feel free to improve this code and 
# use your Python skills to strip that out.