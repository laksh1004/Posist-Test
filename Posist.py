import datetime
class node:                                             #creating node with no values
    def __init__(self, data=None):
        self.data = None
        self.timestamp = datetime.datetime.now()
        self.nodeNum = None
        self.nodeID = None
        self.children = []
        self.parentID = None
        self.childID = None
        self.genesis = None

    def addchild(self, obj):
        self.children.append(obj)
        for a in self.children:
            a = node(a)



class dynlist:


    def __init__(self):                                 #Initialising the tree
        self.Genesis_Node = node()
        self.head = node()


    def insertGen(self, val, b, c):                     #Making the genesis node
        if(Genesis_Node.data is None):
            Genesis_Node.data = val
            Genesis_Node.timestamp = datetime.datetime.now()
            Genesis_Node.nodeNum = b
            Genesis_Node.nodeID = c
            Genesis_Node.parentID = None
            Genesis_Node.childID = None
            Genesis_Node.genesis = c
        else:
            print("Genesis node is already present!")


    def insertNode(self, val, b, c):                    #creating child nodes
        if val < Genesis_Node.data:

            new_node = node(val)
            new_node.data = val
            new_node.timestamp = datetime.datetime.now()
            new_node.nodeNum = b
            new_node.nodeID = c
            new_node.parentID = None
            new_node.childID = None
            new_node.genesis = c
            cur = self.head
            while cur.childID != None:
                cur = cur.childID
                cur.childID = new_node
