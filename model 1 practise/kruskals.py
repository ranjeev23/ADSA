#create a clsss graph
class Graph:
    
    #initiialize the graph
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    #add edge to graph
    def add_edge(self,source,destn,weight):
        #appends the graph as (source,destn,weight)
        self.graph.append((source,destn,weight))

    def find(self,parent,i):
        print('parent and i',parent,i)
        #recursively find the parent
        if parent[i] != i:
            parent[i] = self.find(parent,parent[i])
        return parent[i]
    
    def union(self,parent,rank,x,y):
        #set y as parent if rank of y is higher
        if rank[x]<rank[y]:
            parent[x] = y
        #set x as parent if rank of x is higher
        elif rank[x]>rank[y]:
            parent[y] = x
        #if the rank is same keep x as parent
        #increament the rank
        else:
            parent[y] = x
            rank[x] += 1

    def kruskalsMST(self):
        result = []
        #2 increament variable one for traversing graph other for increasing edge
        i = 0
        e = 0

        #sort the graph
        self.graph = sorted(self.graph, key=lambda edge:edge[2])

        #set parent and rank as empty list
        parent = []
        rank = []

        #fill parent and rank
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        #loop till edges less than verties-1
        while e< self.V-1:
            #get the source dest and cost of the edge from sorted graph
            source,dest,const = self.graph[i]
            i+=1
            
            #find the source parent and destination parent
            source_parent = self.find(parent,source)
            destn_parent = self.find(parent,dest)

            if source_parent != destn_parent:
                #increament edge
                e+=1
                #append in result
                result.append([source,dest,const])
                #find union of source_parent,destn_parent
                self.union(parent,rank,source_parent,destn_parent)

        min_cost = 0
        for source,dest,cost in result:
            print(f'{source} => {dest} => {cost}')
            min_cost+=cost
        print('min cost',min_cost)

#source_node: {dest_node: edge_length}
graph = {
    0: {
        1: 2799,
        2: 713,
        3: 1631,
        4: 2426,
    },
    1: {
        0: 2799,
        2: 2015,
        3: 1547,
        4: 373,
    },
    2: {
        0: 713,
        1: 2015,
        3: 1086,
        4: 1446,
    },
    3: {
        0: 1631,
        1: 1547,
        2: 1086,
        4: 1180,
    },
    4: {
        0: 2426,
        1: 373,
        2: 1446,
        3: 1180,
    },
}

                
g = Graph(len(graph))

for source_node in graph:
    for dest_node,cost in graph[source_node].items():
        g.add_edge(source_node,dest_node,cost)

g.kruskalsMST()