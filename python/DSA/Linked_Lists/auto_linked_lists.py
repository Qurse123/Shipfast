class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def __iter__(self):  
        node = self.head
        while node is not None:
            yield node
            node = node.next

## traverse a linked list

llist = LinkedList(["a", "b", "c", "d", "e"])

for node in llist:
    print(node)

## for the rest just read about it using roadmap.sh it is useless to copy paste code go build something
