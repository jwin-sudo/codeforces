"""
**Example 1:**
Input: list: 1 → 2 → 2 → 3 → 3, k: 1
Output: 1 → 2 → 3
Explanation: Each value can appear at most once. The second occurrences of 2 and 3 are removed.

**Example 2:**
Input: list: 1 → 1 → 1 → 2 → 2 → 2, k: 2
Output: 1 → 1 → 2 → 2
Explanation: Each value can appear at most twice. The third occurrence of both 1 and 2 is removed.

**Example 3:**
Input: list: 1 → 2 → 1 → 2 → 1, k: 1
Output: 1 → 2
Explanation: Non-consecutive duplicates are also counted and removed after the first occurrence.


Edge cases/Assumptions/Observations :
- k could be higher than frequency of elements - just preserve the entire LL in that case
- if k = 0, return null


Approach :
- Initialize the hashmap
get a dummy node with next set to head
assign prev to dummy node and curr to head
iterate through the entire LL
if at each node the occurance is greater than K  then
make prev.next is pointing to curr.next
and curr=curr.next
else:
curr=curr.nect and prev=prev.next
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def array_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def limitToKTimesLL(head, k):
    freq = {}
    dummy = ListNode(0, head)
    prev = dummy
    curr = head

    while curr:
        freq[curr.val] = freq.get(curr.val, 0) + 1

        if freq[curr.val] > k:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = prev.next
            curr = curr.next
    return dummy.next


# Test 1: Basic case - k=1 keeps only first occurrence
head = array_to_list([1, 2, 2, 3, 3])
result = limitToKTimesLL(head, 1)
assert list_to_array(result) == [1, 2, 3], "Test 1 failed"

# Test 2: k=2 allows two repetitions
head = array_to_list([1, 1, 1, 2, 2, 2])
result = limitToKTimesLL(head, 2)
assert list_to_array(result) == [1, 1, 2, 2], "Test 2 failed"

# Test 3: Empty list
result = limitToKTimesLL(None, 1)
assert result is None, "Test 3 failed"

# Test 4: k=0 should return empty list
head = array_to_list([1, 2, 3])
result = limitToKTimesLL(head, 0)
assert result is None, "Test 4 failed"

# Test 5: All same values
head = array_to_list([5, 5, 5, 5, 5])
result = limitToKTimesLL(head, 2)
assert list_to_array(result) == [5, 5], "Test 5 failed"

# Test 6: Non-consecutive duplicates
head = array_to_list([1, 2, 1, 2, 1, 2])
result = limitToKTimesLL(head, 1)
assert list_to_array(result) == [1, 2], "Test 6 failed"

# Test 7: Single element
head = array_to_list([1])
result = limitToKTimesLL(head, 1)
assert list_to_array(result) == [1], "Test 7 failed"

# Test 8: No duplicates - list unchanged
head = array_to_list([1, 2, 3, 4])
result = limitToKTimesLL(head, 1)
assert list_to_array(result) == [1, 2, 3, 4], "Test 8 failed"

print("All tests passed!")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def removeOddsAtOddsLL(head):
    """
        - Initialize prev_idx, cur_idx = 0, 1
    get a dummy node with next set to head
    assign prev to dummy node and curr to head
    iterate through the entire LL
    if at each node cur_idx is odd and cur val is odd
    make prev.next is pointing to curr.next and update hasmaps value of that key by one
    and curr = curr.next
    else:
    update the hashmap value by 1
    curr = curr.nect and prev = prev.next
    """

    prev_idx, curr_idx = 0, 1
    dummy = ListNode(0, head)
    prev = dummy
    curr = head

    while curr:
        if curr_idx % 2 == 1 and curr.val % 2 == 1:
            prev.next = curr.next
            curr_idx += 1
            curr = curr.next
        else:
            curr_idx += 1
            curr = curr.next
            prev = prev.next
    return dummy.next


# Test Case 1: Given example
head1 = list_to_linked([1, 2, 3, 7, 5, 2])
result1 = removeOddsAtOddsLL(head1)
assert linked_to_list(result1) == [2, 7, 2], f"Test 1 failed: {linked_to_list(result1)}"

# Test Case 2: Empty list
result2 = removeOddsAtOddsLL(None)
assert result2 is None, "Test 2 failed"

# Test Case 3: Single odd element (removed)
head3 = list_to_linked([5])
result3 = removeOddsAtOddsLL(head3)
assert linked_to_list(result3) == [], f"Test 3 failed: {linked_to_list(result3)}"

# Test Case 4: Single even element (kept)
head4 = list_to_linked([4])
result4 = removeOddsAtOddsLL(head4)
assert linked_to_list(result4) == [4], f"Test 4 failed: {linked_to_list(result4)}"

# Test Case 5: All even numbers (no removals)
head5 = list_to_linked([2, 4, 6, 8])
result5 = removeOddsAtOddsLL(head5)
assert linked_to_list(result5) == [
    2,
    4,
    6,
    8,
], f"Test 5 failed: {linked_to_list(result5)}"

# Test Case 6: All odd numbers
head6 = list_to_linked([1, 3, 5, 7])
result6 = removeOddsAtOddsLL(head6)
assert linked_to_list(result6) == [3, 7], f"Test 6 failed: {linked_to_list(result6)}"

# Test Case 7: Odd numbers only at even positions (no removals)
head7 = list_to_linked([2, 1, 4, 3, 6, 5])
result7 = removeOddsAtOddsLL(head7)
assert linked_to_list(result7) == [
    2,
    1,
    4,
    3,
    6,
    5,
], f"Test 7 failed: {linked_to_list(result7)}"

print("All tests passed!")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linkedListToArray(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def minTwoLL(head1, head2):
    curr1 = head1
    curr2 = head2

    while curr1 and curr2:
        curr1.val = min(curr1.val, curr2.val)

        curr1 = curr1.next
        curr2 = curr2.next

    return head1


# Test Case 1: Basic case with alternating minimums
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head2 = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
result = minTwoLL(head1, head2)
assert linkedListToArray(result) == [1, 2, 3, 2, 1], "Test 1 Failed"

# Test Case 2: All values from first list are smaller
head1 = ListNode(1, ListNode(2, ListNode(3)))
head2 = ListNode(4, ListNode(5, ListNode(6)))
result = minTwoLL(head1, head2)
assert linkedListToArray(result) == [1, 2, 3], "Test 2 Failed"

# Test Case 3: All values from second list are smaller
head1 = ListNode(4, ListNode(5, ListNode(6)))
head2 = ListNode(1, ListNode(2, ListNode(3)))
result = minTwoLL(head1, head2)
assert linkedListToArray(result) == [1, 2, 3], "Test 3 Failed"

# Test Case 4: Equal values at some positions
head1 = ListNode(1, ListNode(3, ListNode(5)))
head2 = ListNode(1, ListNode(2, ListNode(5)))
result = minTwoLL(head1, head2)
assert linkedListToArray(result) == [1, 2, 5], "Test 4 Failed"

# Test Case 5: Single node lists
head1 = ListNode(3)
head2 = ListNode(7)
result = minTwoLL(head1, head2)
assert linkedListToArray(result) == [3], "Test 5 Failed"

# Test Case 6: Both lists are empty
result = minTwoLL(None, None)
assert result is None, "Test 6 Failed"

# Test Case 7: Negative values
head1 = ListNode(-5, ListNode(0, ListNode(5)))
head2 = ListNode(-3, ListNode(-1, ListNode(10)))
result = minTwoLL(head1, head2)
assert linkedListToArray(result) == [-5, -1, 5], "Test 7 Failed"

print("All tests passed!")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def findBiggestDifferencePairLL(head1):
    """
        -take prev is head and curr is head.next
    take max_val to -inf
    iterate over the LL
    if prev.val-curr.val is greater than the max_val
    then update the result variable to [prev.val,curr.val]
    update prev and curr to their next nodes
    """
    if not head1:
        return []

    if not head1.next:
        return []

    prev = head1
    curr = head1.next
    max_val = float("-inf")
    result = [0, 0]

    while curr:
        if abs(prev.val - curr.val) > max_val:
            max_val = abs(prev.val - curr.val)
            result[0] = prev.val
            result[1] = curr.val
        prev = curr
        curr = curr.next
    return result


# Test 1: Basic case with max diff in middle
head1 = createLinkedList([1, 2, 3, 10, 4, 11])
assert findBiggestDifferencePairLL(head1) == [3, 10], "Test 1 failed"

# Test 2: Two elements only
head2 = createLinkedList([5, 10])
assert findBiggestDifferencePairLL(head2) == [5, 10], "Test 2 failed"

# Test 3: Negative numbers
head3 = createLinkedList([-5, 5, 3, 4])
assert findBiggestDifferencePairLL(head3) == [-5, 5], "Test 3 failed"

# Test 4: All same values
head4 = createLinkedList([1, 1, 1, 1])
assert findBiggestDifferencePairLL(head4) == [1, 1], "Test 4 failed"

# Test 5: Empty list
head5 = createLinkedList([])
assert findBiggestDifferencePairLL(head5) == [], "Test 5 failed"

# Test 6: Single element
head6 = createLinkedList([5])
assert findBiggestDifferencePairLL(head6) == [], "Test 6 failed"

# Test 7: Decreasing values
head7 = createLinkedList([10, 5, 2, 1])
assert findBiggestDifferencePairLL(head7) == [10, 5], "Test 7 failed"

print("All tests passed!")
