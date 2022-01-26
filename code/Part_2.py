# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:05:00 2020

@author: Morgane
"""

'''

PART 2 :  Professor Layton < Guybrush Threepwood < You

'''

from Graph import Graph
import numpy as np

#STEP 1 : Create the graph

#STEP 2 : Define the 2 different sets of probabe impostors.

def generate_two_sets_impostors(dead, graph):
    #generate the list of possible impostors 1 = the ones who have seen the dead player
    impostor1=[]
    for i in range(0,len(graph[dead])):
        if(graph[dead][i] == 1):
            impostor1.append(i)
            
    #generate the list of possible impostors 2
    impostor2=[]
    for i in range(0,len(graph)):
        if i!= dead :
            impostor2.append(i)
            
    impostors=[impostor1,impostor2]
    return impostors

#STEP 3 : Find the relations between players : who saw who, according to the graph

def generate_edges(graph):
    edges=[]
    for i in range(0,len(graph)):
        for k in range(0,len(graph[i])):
            if(graph[i][k]==1):
                edges.append((i,k))
    return edges


#STEP 4 : According to the 2 different sets of probable impostors, find the different couples of 2 impostors possible

def generate_couple_impostors(dead, graph):
    impostors=generate_two_sets_impostors(dead,graph)
    print("\nThere are two sets of impostors.")
    print("The first impostor is part of this list : ",impostors[0])
    print("The second impostor is part of this list : ",impostors[1])
    
    edges=generate_edges(graph)
    print("\nThe relations between players are :")
    print(edges)
    
    couple_impostors=[]
    for i in range(len(impostors[0])):
        for j in range(len(impostors[1])):
            #if the second impostor is not equal to the first impostor, if the couple is not already in the list (we don't want to have (1 4) and (4 1), and if the second impostor didn't see the first one
            if impostors[0][i] != impostors[1][j] and (impostors[1][j],impostors[0][i]) not in couple_impostors and (impostors[1][j],impostors[0][i]) not in edges:
                couple_impostors.append((impostors[0][i],impostors[1][j]))
    return couple_impostors


def main():
    print("\n PART 2 :  Professor Layton < Guybrush Threepwood < You")

    print("\n QUESTION 1 : Represent the relation (have seen) between players as a graph, argue about your model.")
    

    players=["P0","P1","P2","P3","P4","P5","P6","P7","P8","P9"]
    
    relations=[
        ["P0","P1",1],
        ["P0","P4",1],
        ["P0","P5",1],
        ["P1","P2",1],
        ["P1","P6",1],
        ["P2","P3",1],
        ["P2","P7",1],
        ["P3","P4",1],
        ["P3","P8",1],
        ["P4","P9",1],
        ["P5","P7",1],
        ["P5","P8",1],
        ["P6","P8",1],
        ["P6","P9",1],
        ["P7","P9",1],
    ]
    
    #we create our graph - add the nodes and edges
    graph=Graph()
    graph.add_Nodes(players)
    graph.add_Edges(relations)
    print()
    print(graph)
    
    graph_matrix = graph.generate_adjacency_matrix()
    print("\nThe adjacency matrix of our graph is :")
    print(graph_matrix)
    
    #We converted this matrix into a list of list to simplify our operations
    graph_array = np.asarray(graph_matrix)

    print("\n QUESTION 4 : Implement the algorithm and show a solution.")
    
    final=generate_couple_impostors(0, graph_array) #we look for the possible couples of impostors knowing that 0 is the dead player
    print("\nThe list of possible couples of impostors is :")
    print(final)
    
#main()
    


