# Trees

In case You want to visualise a tree of height upto 5 max with node structure defined as : 

```
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
```
Then,  
You can visualise it by using :  

```
from tree import visualise
visualise(root)            #root is an instance of Node object
```
