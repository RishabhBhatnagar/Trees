from math import log as ln


def visualise(root):
    log2 = lambda x : ln(x)/ln(2)
    
    class RNode:
        def __init__(self, node, n):
            #n defines the number assigned to the node ...a bin number
            self.n = n
            self.data = node.data
            self.right = node.right
            self.left = node.left

    def r_wrap(root):      #implements idea of hamming distance.
    
        def _wrap(node, data):
            '''This function wraps the given node instance to 
            the instance of internal RNode.'''
            
            # copying the node and data
            _root = RNode(node, data)
            
            # recursively copying the left and right child if exists.
            if node.left is not None :
                 # every left child is appended by a 0 or multiplied by 2.
                 # left_child = parent*2 = 2n
                 _root.left = _wrap(node.left, data+'0')
            if node.right is not None :
                 # every right child is appended by a 1 or 
                 # multiplied by 2 and added 1.
                 # right_child = parent*2 + 1 = 2n + 1
                _root.right = _wrap(node.right, data+'1')
            
            return _root
        
        wrapped_root = _wrap(root, '1')  # first node is represented by one.
        return wrapped_root

    def inorder(root, res):
        if root :
            inorder(root.left, res)
            res += [root]
            inorder(root.right, res)
        return res

    pattern = {
        0 : [88, 88],
        1 : [35, 72, 72],
        2 : [16, 36, 34, 36],
        3 : [7, 16, 18, 16, 16, 16, 18, 16],
        4 : [2, 8, 6, 8, 8, 8, 6, 8, 6, 8, 6, 8, 8, 8, 6, 8],
        5 : [2, 4, 2, 2, 2, 4, 2, 4, 2, 4, 2, 2, 2, 4, 2, 2, 2, 4, 2, 2, 2, 4, 2, 4, 2, 4, 2, 2, 2]
    }
    slash_pattern = [1, 4, 8, 18, 36][::-1]
    hat_difference = [None, 73, 34, 16, 6, 0]
    root = r_wrap(root)       # after this, you can use any damn traversal and you can get level_order traversal.
    level_order = sorted(inorder(root, []), key = lambda x : int(x.n, 2)) # directly sort without following loops.
    level_order = {int(node.n, 2) : node   for node in level_order}
    height_tree = __import__("math").ceil(log2(max(level_order.keys())))

    k = 1
    dh = 5-height_tree
    # 5 is the max height that this visualiser can handle.
    
    '''
    # Printing without /\
    for i in range(height_tree):
        n_nodes = 2**i
        for j in range(n_nodes):
            try : print((pattern[i+dh][j])*" ", level_order[k], end="")
            except : print((pattern[i+dh][j])*" ", "--", end="")
            k += 1
        print()
    '''
    if height_tree == 0:
        print(root.data)
        return
    
    for i in range(height_tree):
        n_nodes = 2**i
        print(" ", end='')    #pattern offset
        for j in range(n_nodes):
            try :
                data =  level_order[k].data
                if len(str(data)) < 2 : data = "0"+str(data)
                data = data
                print((pattern[i+dh][j])*" ", data, end="", sep="")
            except:
                print((pattern[i+dh][j])*" ", "--", end="", sep="")
            k += 1
        print()
        
        c = 1
        if i != height_tree - 1:
            for l in range(slash_pattern[i+dh]):
                one_hat = "/" + " "*(2*c) + "\\"
                print(" "*(pattern[i+dh][0]-l), end="")
                for m in range(n_nodes):
                    print(one_hat, sep="", end=" "*(pattern[i+dh][m+1]-2*l-2))
                print()
                c += 1


if __name__ == "__main__":
    
    RED = 1
    BLACK = 2
    
    class Node:
        def __init__(self, data, color=RED):
            self.data = data
            self.right = None
            self.left = None
            self.color = color
    root = Node(8, BLACK)
    root.right = Node(10)
    root.left = Node(3)
    
    root.left.left = Node(1, BLACK)
    root.left.right = Node(6, BLACK)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    visualise(root)
