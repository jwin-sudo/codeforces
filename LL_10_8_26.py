'''
Coding Drills: Linked Lists


Question : 

Given a singly linked list, insert a new node with value 0 after each existing node in the list.
After the operation completes, the resulting list should have exactly twice as many nodes as the original. Every other node (at indices 1, 3, 5, ...) 
should have a value of 0.
Return the head of the modified linked list.

Input:  1 → 2
Output: 1 → 0 → 2 → 0

Input:  5
Output: 5 → 0


Input:  1 → 2 → 3
Output: 1 → 0 → 2 → 0 → 3 → 0


Edge cases/Assumptions/Observations : 
- empty list -> return same
- original list can have zero values


Approach : 

- initialize curr_node and next_node
while curr.node.next is not None
- set curr_node.next to 0
  - update curr_node to where next_node is
  - move up next_node in the LL

Recursive
- base case: 
if node is None:
  return None

# create new node with 0
# track the next node: next_node = node.next
# set the next of curr node to the new node
# new_node.next = recursive_func(next_node)

return curr

Q : Given a singly linked list, a target value, and a replacement value, replace all nodes containing the target value with the replacement value. 
Return the head of the modified linked list.
You may assume the linked list uses the standard singly linked list node structure with val and next properties.

list: 1 → 2 → 3 → 1 → 5, target: 1, replacement: 7
Returns: 7 → 2 → 3 → 7 → 5

list: 4 → 4 → 4, target: 4, replacement: 9
Returns: 9 → 9 → 9

list: 1 → 2 → 3, target: 5, replacement: 10
Returns: 1 → 2 → 3 (no changes since target not found)

Edge cases/Assumptions/Observations : 
- replacing the values only


Approach : 
1. Iterate through the list
2. If the node value is equal to target, replace it with replacement value
3. Else continue
4. Return the head of the list







Q : Given a singly linked list, determine if all the values in the list are unique.
Return true if every node in the linked list contains a distinct value, and false if any value appears more than once.
The linked list is represented by the head node, where each node has a val property containing an integer and a next pointer to the following node (or null/None if it's the last node).


Example 1:
  Input: 1 → 3 → 2
  Output: true
  Explanation: All values (1, 3, 2) are distinct.

Example 2:
  Input: 1 → 6 → 7 → 1 → 9
  Output: false
  Explanation: The value 1 appears twice in the list.

Example 3:
  Input: null (empty list)
  Output: true
  Explanation: An empty list has no duplicates by definition.



Edge cases/Assumptions/Observations : 
- 

Approach : 
- Use a set to track duplicates in list
- return False if any value exists in the set
- return True if we reached the end


Q : Given a singly linked list and a sorted array of indices, return the sum of the values at the nodes located at those indices.
The indices are 0-based (the head of the list is at index 0). The indices array is guaranteed to be sorted in ascending order and contains only valid indices within the bounds of the list.


**Example 1:**
list: 5 → 6 → 7 → 8 → 9, indices: [0, 2, 4]
Output: 21
Explanation: Nodes at indices 0, 2, and 4 have values 5, 7, and 9. Sum = 5 + 7 + 9 = 21

**Example 2:**
list: 1 → 2 → 3 → 4, indices: [1, 3]
Output: 6
Explanation: Nodes at indices 1 and 3 have values 2 and 4. Sum = 2 + 4 = 6

**Example 3:**
list: 10 → 20 → 30, indices: []
Output: 0
Explanation: No indices to sum, so return 0.


Edge cases/Assumptions/Observations : 
- NA

Approach : 
- initialize index_1 to track indices on LL
- initialize index_2 to track indices in the given indices arr
- iterate through LL while incrementing index_1
- if index_1 matches index_2, add nodes val to the sum, increment index_2
- stop when we matched all indices 

*/


/*
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test 1: Basic case
head = create_list([5, 6, 7, 8, 9])
assert sumLLNodesAtIndices(head, [0, 2, 4]) == 21  # 5 + 7 + 9

# Test 2: Single index
head = create_list([1, 2, 3, 4, 5])
assert sumLLNodesAtIndices(head, [3]) == 4

# Test 3: Empty indices array
head = create_list([1, 2, 3])
assert sumLLNodesAtIndices(head, []) == 0

# Test 4: All indices
head = create_list([1, 2, 3])
assert sumLLNodesAtIndices(head, [0, 1, 2]) == 6

# Test 6: Single node list
head = create_list([10])
assert sumLLNodesAtIndices(head, [0]) == 10

# Test 7: First and last indices only
head = create_list([1, 2, 3, 4, 5])
assert sumLLNodesAtIndices(head, [0, 4]) == 6  # 1 + 5

print("All tests passed!")
'''

'''
Input: 1 → 2
Output: 1 → 0 → 2 → 0

Input: 5
Output: 5 → 0


Input: 1 → 2 → 3
Output: 1 → 0 → 2 → 0 → 3 → 0


Edge cases / Assumptions / Observations :
- empty list -> return same
  - original list can have zero values


Approach:

- initialize curr_node and next_node
while curr.node.next is not None
  - set curr_node.next to 0
    - update curr_node to where next_node is
      - move up next_node in the LL

'''

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next 

def insertZero(head):
  curr_node = head 
  


  while curr_node.next:
    next_node = curr_node.next 

    zero = Node(0)
    curr_node.next = zero 
    zero.next = next_node

    curr_node = next_node
  
  curr_node.next = Node(0)

  return head 

def buildLL(node):
  res = ""

  while node:
    res += str(node.value) + "->"
    node = node.next 

  return res[:-2]
head = Node(1, Node(2))
print(buildLL(insertZero(head)))



'''

list: 1 → 2 → 3 → 1 → 5, target: 1, replacement: 7
Returns: 7 → 2 → 3 → 7 → 5
'''

def replacementNode(head, target, replacement):
  curr = head

  while curr:
    if curr.value == target:
      curr.value = replacement
    curr = curr.next 
  return head 
head = Node(1, Node(2, Node(3, Node(1, Node(5)))))
print(buildLL(replacementNode(head, 1, 7)))

'''

list: 4 → 4 → 4, target: 4, replacement: 9
Returns: 9 → 9 → 9
'''
head = Node(4, Node(4, Node(4)))
print(buildLL(replacementNode(head, 4, 9)))

'''
Example 1:
  Input: 1 → 3 → 2
  Output: true
  Explanation: All values (1, 3, 2) are distinct.

Example 2:
  Input: 1 → 6 → 7 → 1 → 9
  Output: false
  Explanation: The value 1 appears twice in the list.

Example 3:
  Input: null (empty list)
  Output: true
  Explanation: An empty list has no duplicates by definition.
'''


def uniqueLL(head):
  if not head:
    return True 
  
  curr = head 
  seen = set()
  while curr:
    if curr.value not in seen:
      seen.add(curr.value)
    else:
      return False 
    curr = curr.next
  return True 

head = Node(1, Node(3, Node(2)))
print(uniqueLL(head))

head = Node(1, Node(6, Node(7, Node(1, Node(9)))))
print(uniqueLL(head))

head = Node(None)
print(uniqueLL(head))

'''
list: 5 → 6 → 7 → 8 → 9, indices: [0, 2, 4]
Output: 21
Explanation: Nodes at indices 0, 2, and 4 have values 5, 7, and 9. Sum = 5 + 7 + 9 = 21

**Example 2:**
list: 1 → 2 → 3 → 4, indices: [1, 3]
Output: 6
Explanation: Nodes at indices 1 and 3 have values 2 and 4. Sum = 2 + 4 = 6

**Example 3:**
list: 10 → 20 → 30, indices: []
Output: 0
Explanation: No indices to sum, so return 0.
'''

def sumOfNodes(head, indices):
  total = 0 
  index_1 = 0
  index_2 = 0 

  while head:
    if index_1 == indices[index_2]:
      total += head.value 
      index_2 += 1
    index_1 += 1
    head = head.next 

  return total 

head = Node(1, Node(2, Node(3, Node(4))))
indices = [1,3]
print(sumOfNodes(head, indices))
    
    
