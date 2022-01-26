# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:37:43 2020

@author: Morgane
"""


'''

PART 4 :  Secure the last tasks

'''

import numpy as np
from Graph import Graph
from collections import deque


# Function which takes the adjacency matrix of a graph and returns a list of routes passing by every node of the graph exactly one time
# In our case : it returns the different routes passing exactly once by every room
# This function needs the recursive function HamiltonRecursif
def Hamilton(adjacency_matrix):
    complete_route=[] # the list of possible routes passing by each room only one time
    
    for i in range (0, adjacency_matrix.shape[0]): #for i in range(0,14) : for every room 
        
        print("starting from room ",i," :")
        # We create a route starting with the room i
        route=[]
        route.append(i) 
        
        # We create a list of impossible routes = routes which can't pass through every room exactly one time
        impossible_route=[]
        
        # We check if there are complete route starting by the room i and add it in the list of complete routes
        HamiltonRecursif(adjacency_matrix, route,impossible_route, complete_route)
    
    # We return the list of possible routes passing by each room exactly once    
    return complete_route
    


def HamiltonRecursif(adjacency_matrix,route,impossible_route, complete_route):

    # if we have a route passing by every room :
    if len(route)==adjacency_matrix.shape[0]: #if len(route)=14
        print(route)
        # We add this route to our list of complete routes (we clone the route or we would have a problem after when we modify the route : it would also modify it in our list of complete_routes)
        clone=list(route)
        complete_route.append(clone)

    # the last room inserted in our route
    last_room=route[-1]
    
    # We create a queue which contains the possible next rooms to visit. It should respect 2 conditions:
    # -the next room should be accessible (a weight different than inf in the adjacency matrix)
    # -the next room shouldn't be already in the route we are creating because each room should be accessed only one time
    possible_next_rooms= deque() 
    for j in range(0,adjacency_matrix.shape[0]):
        if ((adjacency_matrix[last_room,j]!=np.inf) and j not in route):
            possible_next_rooms.append([last_room, j, adjacency_matrix[last_room,j]])
 
    # While there are still rooms we didn't visit yet
    while(len(possible_next_rooms)!=0):

        if len(route)==adjacency_matrix.shape[0]: #if len(route)=14
            break

        else:
            # We create a temporary route in which we add the new room and then check if it becomes an impossible route
            temp_route=list(route) #clone the route
            temp_route.append(possible_next_rooms[0][1])

            # We check if the result obtained is an impossible route or not
            if temp_route in impossible_route:
                # We remove the room (possible_next_rooms[0])from the possible next rooms (as it would lead to an impossible route)
                possible_next_rooms.popleft()
            
            else: # If we are creating a possible route
                # We add for real the room in our route
                route.append(possible_next_rooms[0][1])

                # We remove the room we added from our list of possible next rooms
                possible_next_rooms.popleft()
                
                # We continue to construct our route until the route is either complete or impossible
                HamiltonRecursif(adjacency_matrix, route, impossible_route, complete_route)


    # If we have checked every possibility and either we have only impossible routes or a possible route but we want to check other possibilities (there are maybe more than one possible route starting by the room i)
    if (len(possible_next_rooms)==0):
        new_impossible_route=list(route) #we make a copy of our actual route. If not, there would be a problem when we make route.pop() --> it would also change the new_impossible_route
        if new_impossible_route not in impossible_route:
            impossible_route.append(new_impossible_route)  
            
        # We remove the last room from our route as finally this route is impossible
        route.pop()
            
    return complete_route
     


# Function which returns the fastest routes and its cost (which is the time to travel)
def FastestRoute(possible_routes, adjacency_matrix):
    smallercost=np.inf
    fastest_routes=[]
    
    # We look every route of our possible routes
    for i in range (len(possible_routes)):
        # We compute the total cost of the route = the sum of all the weights 
        cost=0
        for j in range (adjacency_matrix.shape[0]-1):
            cost+=adjacency_matrix[possible_routes[i][j],possible_routes[i][j+1]]

        # If we found a smaller cost
        if cost<=smallercost:
            if cost<smallercost:
                smallercost=cost
                #the fastest route is updated (with the one with a smaller cost)
                fastest_routes=[]
                fastest_routes.append(possible_routes[i])
            else: #cost=smaller_cost
                #we add the route to the fastest_routes
                fastest_routes.append(possible_routes[i])
            
    # We return the fastest routes and its cost
    return fastest_routes, smallercost



def main():

    print("\nPART 4 :  Secure the last tasks")
    
    print("\nQUESTION 4 : Implement the algorithm and show a solution.")
    
    # We create the rooms 
    rooms=["U","L","R","Se","M","E","C","St","W","O2","N","Sh","U?","L?"]
    
    # We create the corridors
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
    
    # We build our graph using our rooms and corridors
    graph_crewmates=Graph()
    graph_crewmates.add_Nodes(rooms)
    graph_crewmates.add_Edges(corridors)
    
    # We create the adjacency matrix of our graph
    adjacency_matrix=graph_crewmates.generate_adjacency_matrix()
    
    # We generate the possible routes which pass through every rooms exactly one time
    print("\nBelow you can see the different possible routes passing by every room exactly one time :")
    possible_routes=Hamilton(adjacency_matrix)
    
    print("In total, there are ",len(possible_routes), " routes passing by every room exactly one time")
    
    # We compute the fastest route between all of them
    fastest_routes, smallercost = FastestRoute(possible_routes, adjacency_matrix)
    print("\nThe fastest routes are :")
    for route in fastest_routes:
        print(route)
    print("If you make no stop during these routes, you take ",smallercost, " seconds to pass through every room.")


#main()
