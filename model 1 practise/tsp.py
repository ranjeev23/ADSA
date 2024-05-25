#travelling salesman problem using DFS BFS AND ID

class TspSolver:

    def __init__(self,graph,initial_node):
        #initialize graph,initial_node,num_nodes,visted_dic,set visited of initial node to True,min cost to inf,optimal path to None
        self.graph = graph
        self.initial_node = initial_node
        self.num_nodes = len(graph)
        self.visited_dic = {node:False for node in self.graph.keys()}
        self.visited_dic[initial_node] = True
        self.min_cost = float('inf')
        self.optimal_path = None
    
    def is_goal_state(self,state):
        #i/p is {A:False,B:False}
        '''
        return a lis of all the nodes that are not visited
        '''
        print(state)
        for bool in state.values():
            if bool is False:
                return False
        return True

    def actions(self,state):
        '''input is a dic of node and bool
           output is lis of all the nodes whose value is False'''
        ret_lis = []
        for node in state:
            #not visited
            if state[node] == False:
                ret_lis.append(node)
        return ret_lis
    
    def pathcost(self,path):
        #set cost 0
        cost = 0
        #iterate through len of path-1
        for index in range(len(path)-1):
            #go to graph find the cost of node at index i, to cost of node at index i+1 from graph
            cost+=self.graph[path[index]][path[index+1]]
        #find the cost of last element at index -1, to cost of node at index 0 from graph
        cost+=self.graph[path[-1]][path[0]]
        return cost

    def DFS(self,cur_node,state=None,path=None,depth=1):
        
        #set the variable
        curr_node = self.initial_node
        if state == None:
            state = self.visited_dic.copy()
        if path == None:
            path =[curr_node]
        
        print(curr_node,state,path,self.num_nodes)
        #if path has eql num of edges
        if depth == self.num_nodes:
            #find the cost of the path
            cost = self.pathcost(path)
            #if cost is less than min cost, update caist and optimalpath
            if cost<self.min_cost:
                self.min_cost = cost
                self.optimal_path = path.copy()

        #loop through nodes that are not yet visited
        for node in self.actions(state):
            #mark the node as True
            #append the node to path
            #recursively call the dfs increament depth
            #to find other paths pop the last node
            #in state set node to False
            state[node] = True
            path.append(node)           
            self.DFS(node,state,path,depth+1)
            path.pop()
            state[node] = False
            
    def bfs(self):
        
        #set a queue of list as #initial_node, #path, #copy of the visited nodes
        queue = [(self.initial_node,[self.initial_node],self.visited_dic.copy())]

        while queue:
            #pop from 0 index and assign the variables
            current_node,path,state = queue.pop(0)
            #if the path is full
            if self.is_goal_state(state):
                #calculate the cost 
                cost = self.pathcost(path)
                #if the cost is less than min cost upadte the mincost and optimal path
                print(path)
                print(cost)
                if cost<self.min_cost:
                    self.min_cost = cost
                    self.optimal_path = path.copy()

            #loop through unvisitedd nodes
            for node in self.actions(state):
                #add the node to new path
                new_path = path + [node]
                #create a copy of the state
                new_state = state.copy()
                #in this set the state of the node to True
                new_state[node] = True
                #append to queue
                queue.append((node,new_path,new_state))

    def iterative_deepening(self):
        for depth_limit in range(1,self.num_nodes + 1):
            self.DFS(self.initial_node,self.visited_dic.copy(),[self.initial_node],1)
                
                    

            

            

#Driver Code

graph1= {
     'A': {'B':30,'C':20},
     'B': {'A':45,'C':34},
     'C': {'A':45,'B':22}
     }
initialnode='A'

tsp=TspSolver(graph1,'A')

# tsp.DFS(initialnode)
# print('BY DFS TRAVERSAL MIN COST=',tsp.min_cost,'OPTIMAL PATH =',tsp.optimal_path)

tsp.iterative_deepening()
print('BY BFS TRAVERSAL MIN COST=',tsp.min_cost,'OPTIMAL PATH =',tsp.optimal_path)



