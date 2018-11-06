def visualise(root):
    from math import log as ln
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
            _root = RNode(node, data)
            if node.left is not None :
                 _root.left = _wrap(node.left, data+'0')
            if node.right is not None : 
                _root.right = _wrap(node.right, data+'1')
            return _root
        root = _wrap(root, '1')
        return root

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
    root = r_wrap(root)       # after this, you can use any traversal and you can get level_order traversal.
    level_order = sorted(inorder(root, []), key = lambda x : int(x.n, 2)) #directly sort without following loops.
    level_order = {int(node.n, 2) : node.data   for node in level_order}
    height_tree = __import__("math").ceil(log2(max(level_order.keys())))

    k = 1
    dh = 5-height_tree

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

    for i in range(height_tree):
        n_nodes = 2**i
        print(" ", end='')    #pattern offset
        for j in range(n_nodes):
            try :
                data =  level_order[k]
                if len(str(data)) < 2 : data = "0"+str(data)
                print((pattern[i+dh][j])*" ", data, end="", sep="")
            except : 
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
    class Node:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None
    root = Node(8)
    root.right = Node(10)
    root.left = Node(3)
    
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    
    root.right.right = Node(14)
    root.right.right.left = Node(13)
    visualise(root)
