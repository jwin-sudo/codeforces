"""
ONE

Given a binary tree, return the count of non-leaf nodes.
A leaf node is defined as a node with no children (both left and right children are null/None). A non-leaf node is any node that has at least one child.
Example(s)
Example 1:
Input:
      1
     / \
    2   3
   /   /
  4   5

Output: 3
Explanation: Nodes 1, 2, and 3 are non-leaf nodes (each has at least one child). Nodes 4 and 5 are leaves.
Example 2:
Input:
    1

Output: 0
Explanation: A single node has no children, so it's a leaf. There are 0 non-leaf nodes.
Example 3:
Input:
    1
   /
  2

Output: 1
Explanation: Node 1 has a left child, making it a non-leaf. Node 2 is a leaf.

if either letf or rigght

 return 1 + function(left) + fucntion(right)



   3  
  5  4
1 2. 6 7 
"""


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def nonLeaf(root):
    count = 0

    def dfs(node):
        nonlocal count
        if not node:
            return

        if node.left or node.right:
            count += 1

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return count


root = Tree(1, Tree(2, Tree(4), None), Tree(3, Tree(5), None))
print(nonLeaf(root))

"""
TWO 
Given a binary search tree that has up to one violating node, return the value of the violating node. When there is a violation, return the lowest node. If there is no violating node, return -1.
Example(s)
**Input:**
          5 
        /    \
      2      10  
       \      
        8     

**Output:** 8 (8 is not less than 5)

plan - 
initialize lower and upper bound to float('-inf') and float('inf')
if val > upperbound or val < lowerbound => return node.val
use dfs to traverse left and right subtree 
   - left -> recurse(left, lowerbound, upperbound would be parent's value)
   - right -> recurse(right, lowerbound would be parent's value, upperbound)

if there's no violation return -1 
if there's violation return node.val 
"""


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def violatingNode(root):
    if not root:
        return -1

    lower = float("-inf")
    upper = float("inf")

    def dfs(node, lower, upper):
        if not node:
            return -1

        if not (lower <= node.val <= upper):
            return node.val

        left = dfs(node.left, lower, node.val)
        right = dfs(node.right, node.val, upper)

        if left != -1:
            return left
        elif right != -1:
            return right
        else:
            return -1

    return dfs(root, lower, upper)


root = Tree(5, Tree(2, None, Tree(8)), Tree(10, None, None))
print(violatingNode(root))


"""
THREE
Given a binary tree and a non-negative integer k representing the maximum depth, truncate the tree so that it only contains nodes at depths 0 through k (inclusive). The root is considered to be at depth 0, its children are at depth 1, and so on.
Modify the tree in-place and return the root of the modified tree.
Example(s)
**Input:**
tree:
          1 
        /   \
       2     3  
      / \   / 
     5   4 6 
          \
           7  

k (depth): 1

**Output:** 
          1 
        /   \
       2     3 


2*(k-1) + 2*(k-2)...

a*(1-r^n)/(1-r)
**Explanation:** The root (1) is at depth 0. Nodes 2 and 3 are at depth 1. Since k=1, we keep all nodes at depths 0 and 1, removing nodes 5, 4, 6, and 7.
Input:
tree:
     1
    / \
   2   3

k (depth): 0
```text

**Output:**
 1

**Explanation:** With k=0, only the root node is kept.
Signature/Prototype
limitToKLevelsBT(root, k)
 queu =[root]
  depth =0
 while queue
 if depth == k:
 for each node in queue
  ndoe.left == null
  node.right == null

  break;

  next_level = [];
  for(node of queue)
  {
        if(node.left) next_lev.push(node.left)
        if(node.right) next_lev.push(node.right)
  }

  queue = next_lev
  depth++;
  }

  return root

FOUR

Given a binary tree and a target value k, count the number of nodes in the tree that have a value strictly larger than k.
Return the count of nodes whose value is greater than k.
Example(s)
Example 1:
Input:
          1 
        /   \
      7       2  
     / \     / \
    3   4   5   3  

k = 4

Output: 2
Explanation: Only nodes with values 7 and 5 are larger than 4.
Example 2:
Input:
      10
     /  \
    5    15

k = 8

Output: 2
Explanation: Nodes with values 10 and 15 are larger than 8.
Example 3:
Input: Empty tree (null)
k = 5

Output: 0
Explanation: No nodes exist in an empty tree.

use dfs to traverse the tree 
check if node.val > k then increment count += 1 
return count 


FIVE

Given the root of a binary tree where each node contains a comparable value, count the number of distinct values present in the tree.
A distinct value is one that we count only once, regardless of how many times it appears across different nodes. For example, if the value 5 appears in three different nodes, it still contributes only 1 to our count.
Return 0 if the tree is empty (root is null).
Example(s)
Example 1:
Input:
    1
   / \
  2   3

Output: 3
Explanation: The tree contains values 1, 2, and 3. All are distinct.
Example 2:
Input:
    2
   / \
  2   3

Output: 2
Explanation: The tree contains values 2, 2, and 3. The distinct values are {2, 3}, so we return 2.
Signature/Prototype
`function countUniqueInTree(root: TreeNode | null): number`

`def count_unique_in_tree(root: Optional[TreeNode]) -> int`

dfs(root, seen)
return seen.length

dfs(root, seen)
{
if node == null return ;
seen.add(node.val);
dfs(root.left, seen);
dfs(root.right, seen)
}

SIX

Given an array of values, construct a binary tree where each node has at most one child, alternating between right and left children. The first child (of the root) should be a right child, the second should be a left child of that right child, and so on, creating a zigzag pattern down the tree.
Return the root of the constructed tree. If the input array is empty, return null (or None in Python).
Example(s)
Example 1:
Input: [1, 2, 3, 4, 5]

Output:
      1
        \
          2
         /
        3
          \
            4
           /
          5
Example 2:
Input: [10, 20]

Output:
      10
        \
          20
Example 3:
Input: []
Output: null

initalize the first value as root 
iterate the array 
create root
isLeft = True
current -= root
for item in array:
  if isLeft:
    curr.left = Node(val)
    curr = curr.left
  else
    curr.right = Node(val)
    curr = curr.left
  isLeft = not isLeft

retrun root
*/
"""
