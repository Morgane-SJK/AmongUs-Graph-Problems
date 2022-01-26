# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:10:22 2020

@author: Morgane
"""

'''

PART 3 :  I don't see him, but I can give proofs he vents!

'''


from Graph import Graph
import numpy as np

#to find the shortest paths between each pair of nodes in the graph
def floyd(adjacency_matrix):
    v = len(adjacency_matrix)

    #we create a clone of the matrix
    distances = np.zeros(adjacency_matrix.shape)
    for i in range(0,v):
        for j in range(0,v):
            distances[i,j] = adjacency_matrix[i,j]
       
    #we calculate the minimum distance between each nodes
    for k in range(0,v):
        for i in range(0,v):
            for j in range(0,v):
                if(distances[i,j] > distances[i,k] + distances[k,j]):
                    distances[i,j] = distances[i,k] + distances[k,j]

    return distances 


#Crewmates' graph
def graph_crewmates(rooms,corridors):
    graph_crewmates=Graph()

    #Add the rooms, which represent the different nodes of our graph
    graph_crewmates.add_Nodes(rooms)

    #Add the corridors, which represent the different edges between our nodes
    graph_crewmates.add_Edges(corridors)
    
    return graph_crewmates


#Impostor's graph
def graph_impostors(rooms,corridors,vents):
    graph_impostors=Graph()

    #Add the rooms
    graph_impostors.add_Nodes(rooms)

    #Add the corridors
    graph_impostors.add_Edges(corridors)
    
    #Add the vents
    graph_impostors.add_Edges(vents)
    
    return graph_impostors
    
    
def shortest_paths_matrix(graph):
    adjacency_matrix=graph.generate_adjacency_matrix()
    shortest_paths_matrix=floyd(adjacency_matrix)
    return shortest_paths_matrix


def main():

    print("\n PART 3 :  I don't see him, but I can give proofs he vents!")
    
    print("\n QUESTION 3 : Implement the method and show the time to travel for any pair of rooms for both models.")
    
    rooms=["U","L","R","Se","M","E","C","St","W","O2","N","Sh","U?","L?"]
    
    corridors=[["U","L",6],["U","R",5],["U","Se",5],["U","M",6],["U","C",8], #corridors between Upper E. and the other rooms
               ["L","R",5],["L","Se",5],["L","E",8],["L","St",10.5],         #corridors between Lower E. and the other rooms
               ["R","Se",4],
               ["M","C",6],
               ["E","St",7.5],
               ["C","St",6.5], ["C","W",5], ["C","U?",6.5],
               ["St","Sh",5],["St","U?",5],["St","L?",4.5],
               ["W","O2",3.5],["W","N",6],["W","Sh",8.5],
               ["O2","N",5.5],["O2","Sh",8],
               ["N","Sh",7.5],
               ["Sh","L?",3.5]]
    
    vents=[["U","R",0],
           ["L","R",0],
           ["Se","M",0],["Se","E",0],
           ["M","E",0],
           ["C","O2",5],["C","N",4.5],["C","Sh",3],["C","U?",0],["C","W",5.5],
           ["W","N",0],["W","U?",5.5],
           ["O2","U?",5],
           ["N","Sh",0],["N","U?",4.5],
           ["Sh","U?",3]]
    
    graph_crewmate=graph_crewmates(rooms,corridors)
    #print(graph_crewmates)
    shortest_paths_crewmates=shortest_paths_matrix(graph_crewmate)
    print("\nThis matrix shows the time to travel between any pair of rooms for a Crewmate (model 1 with only the corridors) :")
    print(shortest_paths_crewmates)
    
    graph_impostor=graph_impostors(rooms,corridors,vents)
    #print(graph_impostors)
    shortest_paths_impostors=shortest_paths_matrix(graph_impostor)
    print("\nThis matrix shows the time to travel between any pair of rooms for an Impostor (model 2 with corridors and vents) :")
    print(shortest_paths_impostors)
    
    
    print("\n QUESTION 4 : Display the interval of time for each pair of room where the traveler is an impostor.")
    
    intervals=shortest_paths_crewmates-shortest_paths_impostors
    print("\nThis matrix represents the interval of time for each pair of room where the traveler is an imposotor. If the value is higher than 0, it means the impostor took a vent so he can be unmasked.")
    print(intervals)


#main()
