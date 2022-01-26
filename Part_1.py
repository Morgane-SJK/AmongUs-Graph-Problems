# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:59:25 2020

@author: Morgane
"""

'''

PART 1 :  To organize the tournament

'''


import random


# QUESTION 1 : a data structure to represent a Player and its Score
# An instance of this class represents a player, which has several attributes : an id, a score and a name
class Player():
    def __init__(self,player_id,player_nom='MynameisRandom',player_score=0,left=None,right=None):
        self.player_id=player_id
        self.player_nom=player_nom
        self.player_score=player_score
        self.left=left
        self.right=right
        self.height = 1
        
    def __str__(self):
        return 'Id='+str(self.player_id)+'   Score='+str(self.player_score)+'   Name='+str(self.player_nom)
    

# QUESTION 2 : a data structure for the tournament
# It is an AVL where each node represents a player
# It has some fuctions typical of an AVL like :
# - get_height
# - balance_factor
# - left_rotate
# - right_rotate
# - insert
# - delete (and get_min_val_node)
class Tournament(): 
    def __init__(self, root=None):
        self.root = root 
        
    #In-Order Traversal of the tree
    def inorder_print(self,root):
        if root:
            self.inorder_print(root.left)
            print(root)
            self.inorder_print(root.right)
    
    def get_height(self, root): 
        if not root: 
            return 0
        return root.height 
  
    def balance_factor(self, root): 
        if not root: 
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    #Left rotation
    def left_rotate(self, z):
        y = z.right
        temp = y.left
        y.left = z
        z.right = temp

        z.height = 1 + max(self.get_height(z.left),self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        
        return y

    # Right rotation
    def right_rotate(self, z):
        y = z.left
        temp = y.right
        y.right = z
        z.left = temp

        z.height = 1 + max(self.get_height(z.left),self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),self.get_height(y.right))
        
        return y    
    
    
    def insert(self, root, pid,pnom='MynameisRandom',pscore=0): 
      
        if not root: 
            return Player(pid,pnom,pscore)
            
        elif pid < root.player_id: 
            root.left = self.insert(root.left, pid,pnom,pscore) 
        else: 
            root.right = self.insert(root.right, pid,pnom,pscore) 
  
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right)) 
  
        balance = self.balance_factor(root)
        
        if balance > 1 and pid < root.left.player_id:
            return self.right_rotate(root)
        
        if balance < -1 and pid > root.right.player_id:
            return self.left_rotate(root)
        
        if balance > 1 and pid > root.left.player_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and pid < root.right.player_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def get_min_val_node(self,root): 
        current = root 
        while(current.left is not None): 
            current = current.left   
        
        return current.player_id
    
    def delete(self, root, pid):
        if not root:
            return root
        
        elif pid < root.player_id:
            root.left = self.delete(root.left, pid)
            
        elif pid > root.player_id:
            root.right = self.delete(root.right, pid)
            
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.get_min_val_node(root.right)
            root.player_id = temp
            root.right = self.delete(root.right, temp)

        if root is None:
            return root
        
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))

        balance = self.balance_factor(root)
        
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.balance_factor(root.right) < 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    
# QUESTION 3 : randomize player score

    def random_score(self):
        return random.randint(0,12)
    
    
# QUESTION 4 : randomize player score
        
    # We look for the player we want to update the score
    def search_player(self,root,pid):
        if(root is None or root.player_id == pid):
            return root
        if(root.player_id<pid):
            return self.search_player(root.right,pid)
        return self.search_player(root.left,pid)
    
    # We update the score of the player
    def update_database(self,root,pid,newscore):
        r=self.search_player(root,pid)
        if r is None:
            print("This player doesn't play in this competition.")
        else:
            r.player_score = r.player_score + newscore
            

# QUESTION 5 : create random games based on the database

    # We fill a table with the nodes
    def inorder_fill_table(self,start,table):
        if start:
            if start.left is not None:
                self.inorder_fill_table(start.left,table)
            table.append(start)
            if start.right is not None:
                self.inorder_fill_table(start.right,table)
             
    # we create batchs of nbPlayers players
    def create_games_database(self,root,nbPlayers):
        l = []
        self.inorder_fill_table(root,l)
        random.shuffle(l)
        teams = [ l[i:i+nbPlayers] for i in range(0,len(l),nbPlayers) ]
        
        return teams
    

# QUESTION 6 : create games based on ranking  
        
    def create_games_ranking(self,root,nbPlayers):
        l = []
        self.inorder_fill_table(root,l)
        l.sort(key=lambda node: node.player_score,reverse=True)
        teams = [ l[i:i+nbPlayers] for i in range(0,len(l),nbPlayers) ]
        
        return teams
    

# QUESTION 7 : drop the players and play until the last 10 players
    
    def inOrder(self, root): 
        
        if root:
            return (self.inOrder(root.left) + [root.player_id] + self.inOrder(root.right)) 
        
        else:
            return []    
  
    def play_until_10_left(self,root,nbPlayers):
        
        tree = self.inOrder(root)
        while(len(tree)>nbPlayers):
            
            print("\nThe id of the players still in the tournament are : ",tree)
        
            l = self.create_games_ranking(root,nbPlayers)

            for batch in l:
                for player in batch:
                    for j in range(0,3):
                        self.update_database(root,player.player_id,self.random_score())

            nodes = []
            self.inorder_fill_table(root,nodes)
            nodes.sort(key=lambda node: node.player_score)
            print("The leaderboard after playing is")
            for b in nodes:
                print(b)
            
            
            print("\nThe following players are going to be ejected from the tournament :")
            for node in nodes[0:nbPlayers]:
                print(node)
                self.delete(root,node.player_id)
            
            tree = self.inOrder(root)

        print("\nThe 10 final players are : ")
        self.inorder_print(root)


# QUESTION 8 : final game which displays the TOP10 and the podium
    
    # We reinitialize all the scores to 0
    def reinitialize(self,start):
        if start:
            start.player_score=0
            self.reinitialize(start.left)
            self.reinitialize(start.right)
            
    def final_ranking(self,root):
        self.reinitialize(root)
        
        batch = []
        self.inorder_fill_table(root,batch)
        
        print("\nAs we reinitialized all scores, the leaderboard before playing the final game is : ")
        for a in batch:
            print(a)

        for player in batch:
            for j in range(0,5):
                self.update_database(root,player.player_id,self.random_score())
        
        print("\nThe leaderboard after playing 5 games :")
        for a in batch:
            print(a)

        batch.sort(key=lambda node: node.player_score,reverse=True)
        
        print("\nThe TOP 10 Players is : ")
        for b in batch:
            print(b)
        
        print("\nThe PODIUM is : ")
        for b in batch[0:3]:
           print(b)
        print("CONGRATULATIONS !!!")
       


def Q1():
    print("\nA player is represented by its id, score and name.")
    player1 = Player(1,"John")
    print(player1)
    
    
def Q2():
    print("\nWe create a tournament and insert 10 players inside it.")
    t=Tournament()
    t.root = None
    t.root=t.insert(t.root,1,"John")
    t.root=t.insert(t.root,2,"anonymous34")
    t.root=t.insert(t.root,3,"RedKing")
    t.root=t.insert(t.root,4,"banana18")
    t.root=t.insert(t.root,5,"momo98")
    t.root=t.insert(t.root,6,"dontkillmeplease")
    t.root=t.insert(t.root,7,"distraction")
    t.root=t.insert(t.root,8,"bobby15")
    t.root=t.insert(t.root,9,"blueparth")
    t.root=t.insert(t.root,10,"OrangeQueen")
    print("The players of our tournament are : ")
    t.inorder_print(t.root)

    return t

def Q3_4(tournament):
    print("\nAfter updating the score of player 1 we have :")
    tournament.update_database(tournament.root, 1, tournament.random_score())
    tournament.inorder_print(tournament.root)
    
    print("\nAfter updating again the score of player 1 we have :")
    tournament.update_database(tournament.root, 1, tournament.random_score())
    tournament.inorder_print(tournament.root)
    
    print("\nAfter updating the score of player 12 we have :")
    tournament.update_database(tournament.root, 12, tournament.random_score())
    tournament.inorder_print(tournament.root)
        

def Q_expand_tournament(t):
    t.root=t.insert(t.root, 11, "professorlayton", 4)
    t.root=t.insert(t.root, 12, "darkxor", 3)
    t.root=t.insert(t.root, 13, "ihavecovid19", 11)
    t.root=t.insert(t.root, 14, "rainbow84", 2)
    t.root=t.insert(t.root, 15, "impostor14", 10)
    t.root=t.insert(t.root, 16, "invisibleh24", 5)
    t.root=t.insert(t.root, 17, "Nyhrox", 3)
    t.root=t.insert(t.root, 18, "Aqua", 2)
    t.root=t.insert(t.root, 19, "Rojo", 15)
    t.root=t.insert(t.root, 20, "Wolfiez", 12)
    t.root=t.insert(t.root, 21, "Falconer", 5)
    t.root=t.insert(t.root, 22, "Megga", 2)
    t.root=t.insert(t.root, 23, "Skite", 10)
    t.root=t.insert(t.root, 24, "Fatch", 13)
    t.root=t.insert(t.root, 25, "Crue", 8)
    t.root=t.insert(t.root, 26, "Kreo", 7)
    t.root=t.insert(t.root, 27, "EpikWhale", 5)
    t.root=t.insert(t.root, 28, "Zexrow", 6)
    t.root=t.insert(t.root, 29, "Bugha", 4)
    t.root=t.insert(t.root, 30, "Vato", 3)
    return t


def Q5_6(tournament):
    
    print("\n*** We create random teams *** ")
    random_teams= tournament.create_games_database(tournament.root,10)

    for teams in random_teams:
        print("---The players of the team are :")
        for player in teams:
            print(player)
        
        
    print()
    print("\n*** We create teams based on ranking *** ")
    ranking_teams= tournament.create_games_ranking(tournament.root,10)

    for teams in ranking_teams:
        print("---The players of the team are :")
        for player in teams:
            print(player)
    print()
        
def Q7(tournament):
    tournament.play_until_10_left(tournament.root,10)
    
def Q8(tournament):
    tournament.final_ranking(tournament.root)
    
   
    
def main():
    
    print("\n PART 1 :  TO ORGANIZE THE TOURNAMENT")
    
    print("\n QUESTION 1 : a player and its score")
    Q1()
    
    print("\n QUESTION 2 : the tournament")
    tournament=Q2()
    #print(tournament)
    
    print("\n QUESTIONS 3-4 : update Players score and the database with random scores")
    Q3_4(tournament)
    
    print("\n For the next questions, we decided to insert 20 new players in our tournament in order to have enough players to test our functions. We gave them non null scores in order to check if games on ranking is efficient.")
    Q_expand_tournament(tournament)
    
    print("\n QUESTIONS 5-6 : create random games based on the database or games based on ranking")
    Q5_6(tournament)
    
    print("\n QUESTIONS 7 : drop the players and play until we have only 10 players")
    Q7(tournament)
    
    print("\n QUESTIONS 8 : final game between the 10 last players")
    Q8(tournament)

    
   
#main()


