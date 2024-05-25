#huffman Node class
class huffmanNode:
    #initialize val freq left right 
    def __init__(self, freq, val=None, left=None, right=None):
        self.freq = freq
        self.left = left
        self.right = right
        self.val = val
        pass
    
    #override less than operation
    def __lt__(self,other):
        if self.freq < other.freq:
            return True
        else:
            return False
    
    #override equal to operations
    def __eq__(self,other):
        if self.frq == other.freq:
            return True
        else:
            return False

#main class to implement huffmancoding   
class huffmanencoding:
    
    #initialize the varialble
    def __init__(self,txt):
        self.txt = txt
        self.lis = []
        self.tree = None
        self.code_dict = {}
        self.root = None

    #find freq and return as list of tuples
    def freq_lot(self):
        #sets the list as frq of tuples
        '''
        create a freq distribution of characters
        create a list of tuple by list comprehension
        pass this lot
        '''
        for char in self.txt:
            if char not in self.code_dict:
                self.code_dict[char]=1
            else:
                self.code_dict[char]+=1
        print(self.code_dict)
    
    #func to convert list of tuples to list of nodes
    def converttoNode(self):
        #change lis itself
        '''
        input: code_dict
        output: convert to nodelist and return it
        '''
        dict = self.code_dict
        lot = [(k,v) for k,v in dict.items()]
        for tup in lot:
            self.lis.append(huffmanNode(tup[1],tup[0]))
        print(self.lis)
    
    #combine two nodes
    def combineTwoNodes(self,n1:huffmanNode,n2:huffmanNode):
        #o/p is a new node with empty value and cum freq of n1 and n2
        '''
        store freq of n1, n2 in com_freq
        create a new node with com_freq
        set the new node left,n new node right as n1, n2
        return the new node
        '''
        f_1 = n1.freq
        f_2 = n2.freq
        com_freq = f_1+f_2
        new_node = huffmanNode(com_freq)
        new_node.left = n1
        new_node.right = n2
        return new_node

    #sort the nodes
    def sortNodes(self):
        #sort the nodes in lis
        '''
        return sorted nodes_lis
        '''
        self.lis = sorted(self.lis)
        val_lis = [val.val for val in self.lis]
        print(val_lis)

    #create the tree
    def con_lis_Tree(self):
        #set tree variable to Tree
        '''
        loop till len of list == 1:
            pop 2 nodes
            combine the 2 nodes
            append in nodeList
            sort the node list
        return nodelist
        '''
        while len(self.lis) > 1:
            n1 = self.lis.pop(0)
            n2 = self.lis.pop(0)
            print(n1.val,n2.val)
            new_node = self.combineTwoNodes(n1,n2)
            self.root = new_node
            self.lis.append(new_node)
            self.sortNodes()
        

        print(self.lis)
        print(self.root.val,self.root.freq)
        
    
    #travers the tree
    def traverse(self,node,path = ''):
        #maybe set a class variable and store the paths of the node as output
        '''
        if node is none
            retunr
        if node value is not none
            code_dict[node.val] = path
        self.traverse(node.left,path+'0')
        self.travers(node.right,pathe+'1')
        '''
        if node is None:
            return 
        else:
            if node.val is not None:
                print(node,node.val,node.freq,path)
        self.traverse(node.left,path+'0')
        self.traverse(node.right,path+'1')
    
    

    #act as the facade
    def buildhuffman(self):
        self.freq_lot()
        self.converttoNode()
        self.sortNodes()
        self.con_lis_Tree()
        self.traverse()
        print(self.code_dict)

huff = huffmanencoding('1223334444')
huff.freq_lot()
huff.converttoNode()
huff.sortNodes()
huff.con_lis_Tree()
huff.traverse(huff.root)



        
    


    