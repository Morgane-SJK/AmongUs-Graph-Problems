# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:01:14 2020

@author: Morgane
"""

'''

We use this graph in the STEPS 2, 3 and 4.

'''


import numpy as np

class Graph:
    
    def __init__(self):
        self.nodes={} #dictionary of node: the key is the name of the node (either a player name for STEP2 or a name of room for STEP3 and STEP4) and the value is an integer
        self.edges=[] #list of edges
        
    def __str__(self):
        return ("The graph is made of "+str(len(self.nodes))+" nodes and "+str(int(len(self.edges)/2))+" edges. \nThe nodes are :"+str(self.nodes.items()))
    
    #to add one or several nodes in our dictionary
    def add_Nodes(self, n):
        if type(n)==str or type(n)==int:
            self.nodes[n]=len(self.nodes)
        if type(n)==list:
            for item in n:
                self.nodes[item]=len(self.nodes)
    
    #to add one edge 
    def add_Edge(self, n1, n2, w): #n1=node 1, n2=node 2, w=weight of the edge
        if (n1 in self.nodes.keys() and n2 in self.nodes.keys()):
            self.edges.append([self.nodes[n1],self.nodes[n2],w])
            self.edges.append([self.nodes[n2],self.nodes[n1],w]) #because our graph is not directed
    
    #to add a list of edges
    def add_Edges(self, new_edges_list):
        for new_edge in new_edges_list:
            self.add_Edge(new_edge[0],new_edge[1],new_edge[2])
            
    #we create the adjacency matrix using the package numpy
    def generate_adjacency_matrix(self):
        adjacency_matrix=np.matrix(np.ones((len(self.nodes),len(self.nodes))) * np.inf)

        np.fill_diagonal(adjacency_matrix,0)
        for edge in self.edges:
            if edge[2]<adjacency_matrix[edge[0],edge[1]]: #add the new weight only if it is smaller than the one possibly already in the matrix
                adjacency_matrix[edge[0],edge[1]]=edge[2]
        return adjacency_matrix
    
