#class Node
class Node:
    #initialize data parent left right
    def __init__(self,data=None,parent=None,left=None,right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

#class SplayTree
class SplayTree:
    #initialize root as None
    def __init__(self,root):
        self.root = root
    
    #func maximum 
    def maximum(self,x):
        #[go to right,if no right element exist return last element]
        el = x
        while el.right is not None:
            el = el.right
        return el
            
    
    #func left rotate
    def left_rotate(self,x):
        #func will left rotate the given noe
        '''
        draw diagram of graph
        we can see that only 4 nodes change
        find the right logic to perform left rotation
        '''
        #set y
        y = x.right

        #set y.left
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        #set parent of y 
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x==x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        #set x
        y.left = x
        x.parent = y
    
    #func right rotate
    def right_rotate(self,x):
        #func will right rotate the given node
        '''
        draw diagram of graph
        we can see that only 4 nodes change
        find the right logic to perform right rotation
        '''
        #sety
        y = x.left

        #set y.right
        if y is not None:
            x.left = y.right
            if y.right is not None:
                y.right.parent = x

        #set parent of y
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        #set x
        y.right = x
        x.parent = y

    #func to splay 
    def splay(self, n):
        #will bring the given given node to root
        '''
        loop till parent is not None
            if n.parent is root
                rotate accordingly to bring n to root
            else
                find parent and grand parent of n
                write the 4 conditions and perform the correct order of rl rotations    
        '''
        while n.parent is not None:
            print('inn')
            if n.parent == self.root:
                if n == n.parent.left:
                    self.right_rotate(n.parent)
                else:
                    self.left_rotate(n.parent)
            else:   
                p = n.parent
                g = p.parent
                if p.left == n and p.parent.left == p:
                    self.right_rotate(g)
                    self.right_rotate(p)
                if p.right == n and p.parent.right == p:
                    self.left_rotate(g)
                    self.left_rotate(p)
                if p.left == n and p.parent.right == p:
                    self.right_rotate(p)
                    self.left_rotate(g)
                if p.right == n and p.parent.left == p:
                    self.left_rotate(p)
                    self.right_rotate(g)
    
    #func to insert
    def insert(self, n):
        #insert based on normal bst, will bring the node to root
        '''
        find the optimal parent of n as y
        set n's parent as y
        correctly set n as y child either left or right
        splay the last inserted node
        '''
        #find optimal parent
        n = Node(n)
        #set variables
        y = None
        temp = self.root
        #loop through to find parent
        while temp is not None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        n.parent = y
        #set parents left or right
        if y is None:
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n
        #splay the tree
        self.splay(n)   

    
    #func to search
    def search(self,n,x):
        #returns the matching node and splays to root
        '''
        n => node
        x => value to search
        check if n.data is x
            if true splay node
        if n.data < x
            return search(n.right,x)
        if n.data > x
            returm search(n.left,x)
        '''
        if n.data == x:
            print(n,n.data,x)
            return n
        if n.data<x:
            return self.search(n.right,x)
        else:
            return self.search(n.left,x)

    #func to delete
    def _delete(self,n):
        '''
        splay n

        initialize left subtree as empty splay tree
        set left subtree root as current trees root left
        set the left subtrees roots parent if root is not None
        initialize right subtree as empty splay tree
        set right subtree root as current trees root.right
        set the right subtree roots parent if it not None

        if left subtree root is not None
            find maximum in left subtree
            splay the max node
            after splaying the left subtree of root will be empty
            set the right of root of left subtree to right subtree.root
            set the self.root to left subtree.root
            set the parent of right subtree as left subtreee root
        '''
        self.splay(n)

        self.inorder()

        #set root as left and its parent as None
        left_subtree = SplayTree(n.left)
        if n.left is not None:
            left_subtree.root.parent = None
            
        #set root as right and its parent as None
        right_subtree = SplayTree(n.right)
        if n.right is not None:
            right_subtree.root.parent = None

        if left_subtree.root is not None:
            #find max from left subtree and set its right to rightsubtree
            maxi = self.maximum(left_subtree.root)
            left_subtree.splay(maxi)

            left_subtree.root.right = right_subtree.root
            self.root = left_subtree.root

            #remove data from right subtree
            right_subtree.root.parent = self.root
            right_subtree.root = None

    def delete(self,x):
        el = self.search(self.root,x)
        print(el.data)
        self._delete(el)
        
    #print inorder traversal
    def _inorder(self,n,level=0,prefix=''):
        #just prints inorder
        '''
        if n is not none
        inorder(n.left)
        print n
        inorder(n.right)
        '''
        if n is not None:
            self._inorder(n.left,level+1,prefix+'L: ')
            print(' '*4*level+prefix+str(n.data))
            self._inorder(n.right,level+1,prefix+'R: ')
    
    def inorder(self):
        self._inorder(self.root)
            
        


# Create the binary tree
st = Node(10)
st.right = Node(15)
st.right.parent = st  # Set parent pointer
st.right.right = Node(20)
st.right.right.parent = st.right  # Set parent pointer
st.right.left = Node(13)
st.right.left.parent = st.right  # Set parent pointer
st.right.left.left = Node(12)
st.right.left.left.parent = st.right.left  # Set parent pointer
st.right.left.right = Node(14)
st.right.left.right.parent = st.right.left  # Set parent pointer
st.left = Node(5)
st.left.parent = st  # Set parent pointer
st.left.right = Node(8)
st.left.right.parent = st.left  # Set parent pointer
st.left.left = Node(3)
st.left.left.parent = st.left  # Set parent pointer
st.left.right.left = Node(6)
st.left.right.left.parent = st.left.right  # Set parent pointer
st.left.right.right = Node(9)
st.left.right.right.parent = st.left.right  # Set parent pointer
st.left.left.left = Node(1)
st.left.left.left.parent = st.left.left 

Splay_tree = SplayTree(st)

def inorder_traversal(root, traversal):
    if root:
        inorder_traversal(root.left, traversal)
        traversal.append(root.data)
        inorder_traversal(root.right, traversal)

def visualize_inorder_traversal(root, level=0, prefix=''):
    if root:
        visualize_inorder_traversal(root.left, level + 1, 'L: ')
        print(' ' * (level * 4) + prefix + str(root.data))
        visualize_inorder_traversal(root.right, level + 1, 'R: ')

# Printing the root data of the SplayTree instance
print("Root data of Splay Tree:", Splay_tree.root.data)

# Finding and printing the maximum value in the tree
print("Maximum value in the tree:", Splay_tree.maximum(st).data)

# Visualizing the inorder traversal along with the tree structure
print("\nTree Structure with Inorder Traversal:")
visualize_inorder_traversal(Splay_tree.root)


# Performing a left rotation on the tree
Splay_tree.splay(st.left.left.left)

# Visualizing the inorder traversal along with the tree structure
print("\nTree Structure with Inorder Traversal:")
visualize_inorder_traversal(Splay_tree.root)

Splay_tree.search(st,9)

Splay_tree.insert(12.5)
Splay_tree.insert(30)
Splay_tree.insert(29)

# Visualizing the inorder traversal along with the tree structure
print("\nTree Structure with Inorder Traversal:")
visualize_inorder_traversal(Splay_tree.root)

Splay_tree.inorder()

Splay_tree.delete(12.5)


Splay_tree.inorder()

Splay_tree.delete(29)

Splay_tree.inorder()