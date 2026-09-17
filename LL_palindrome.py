class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 

def buildLL(node):
    res = ""
    
    while node:
        res += str(node.value) + "->"
        node = node.next 
    
    return res[:-2]

def reverseLL(head):
    original = head 
    
    tail = None 
    while original: 
        next_node = original.next 
        original.next = tail 
        
        tail = original 
        original = next_node
     
    while head and tail:
        if head.value != tail.value:
            return False
        head = head.next
        tail = tail.next
    
    return True  

head = Node(1, Node(2, Node(1)))
print(reverseLL(head))         
    
    