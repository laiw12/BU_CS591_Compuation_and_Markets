#Shirui Ye
import scipy.io
import requests
import networkx as nx
import matplotlib.pyplot as plt
import re
import scipy

response = requests.get('https://escience.rpi.edu/data/DA/fb100/')
html = response.text
tokens = re.split('>|<', html)
files = [token for token in tokens if token[-3:] == 'mat' and token != 'schools.mat']


l=len(files)

Xvalue = [0 for x in range(l)]
Yvalue = [0 for y in range(l)]


for n in range(l):
    d={}
    scipy.io.loadmat(files[n],d)
    Ini=0
    for keys,values in d.items():
        if keys=="A":
            p=values
    Graph=nx.Graph(p)
    A=Graph.degree(Graph.nodes())
    length=len(Graph.degree())
    edge=2*Graph.number_of_edges()
    averagefriends=edge/Graph.number_of_nodes()
    k=0
    while k!=len(Graph.degree()):
       
    #for m in range(length):
        Ini=Ini+(Graph.degree()[k])**2
        k=k+1
    v=2*Graph.number_of_edges()
    averagefriendsoffriends=Ini/v
    Xvalue[n]=averagefriends
    Yvalue[n]=averagefriendsoffriends
    print(averagefriends)
    print(averagefriendsoffriends)
             
        


plt.scatter(Xvalue,Yvalue,s=100,c='grey')
plt.ylabel('average number of friends of friends')
plt.xlabel('average number of friends')


      
     


