class Node:
    def __init__(self,data):
            self.data = data 
            self.next = None
    def __repr__(self):
            return self.data

class LinkedList:
    def __init__(self):
        self.head = None ## inital head of the node returns nothing or none 
    
    def __repr__(self): ## helps us define how we represent the nodes
        node = self.head ## tells us the head of the node has no values as of now so its defined as none shows that the linked list terminates
        nodes = [] ## the variable node gies us [] if we print this as is it would just give us []
        while node is not None: ## while loop, node is not none ie value assigned to a node 
            nodes.append(node.data) ## append the varaible nodes and within the list[] add the data assigned to the node ie node(a) data = "a"
            node = node.next ## the current head is now a defined as node = self.head and is now points to the next item in the list making it a linked list
        nodes.append("None") ## now the linked list we created of [a] is incomplete using this variable we now say that the nodes which contains node (a) points to the string None 
        return " -> ".join(nodes) ## creates a linked list of [a --> none]


llist = LinkedList()
print(llist) ## prints nothing as llist which is the class linkedList is defined as None with the head of that "list" being the sting none

first_node = Node("a")  ## now defined a node called first_node ... so node(a) says our data or simantically our self.data = data, this node exists but it not linked to anything
llist.head = first_node ## You have now defined that our first node of a is the head of the  list
print(llist) ## creates a linked list of [a --> none]



second_node = Node("b")
third_node = Node("c")
first_node.next = second_node ## our second node is now the sitting in index 2
second_node.next = third_node ## our third node is now the sitting in index 3
## the "none" string is our index 4 
print(llist)