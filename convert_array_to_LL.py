class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 
        
def convert_array_to_LL(array):
    head = Node(0, None)
    dummy = head 
    for num in array:
        head.next = Node(num, None)
        head = head.next 
    
    return dummy.next 

def buildLL(node):
    res = ""
    while node:
        res += str(node.value) + "->"
        node = node.next 
    return res[:-2]

array = [1,2,3]
print(buildLL(convert_array_to_LL(array)))