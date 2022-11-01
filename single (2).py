class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node
    

    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self,values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
        
    def __str__(self):
            return ' -> '.join([str(node) for node in self])    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count  
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next    
    @property
    def values(self):
        return [node.value for node in self]    
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail    
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
class SocialMediaManager(LinkedList):
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        return self    
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            current_head = self.head
            self.head = Node(value, current_head)
            current_head.prev = self.head
        return self.head
socialMediaManager = SocialMediaManager()
# would store the name and the likes
postone=dict()
postone["girma"]=33 #likes
posttwo=dict()
posttwo["abebe"]=45

socialMediaManager.add_node(postone)
socialMediaManager.add_node(posttwo)
def display():
    size = socialMediaManager.__len__()-1
    print(socialMediaManager.values[size])
display()