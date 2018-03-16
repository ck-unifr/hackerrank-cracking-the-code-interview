# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem

# A linked list is said to contain a cycle if any node is visited more than once while traversing the list.


# Complete the function provided in the editor below. It has one parameter: a pointer to a Node object named head
# that points to the head of a linked list.
# Your function must return a boolean denoting whether or not there is a cycle in the list.
# If there is a cycle, return true; otherwise, return false.

# Note: If the list is empty, head will be null.

# Input Format

# Our hidden code checker passes the appropriate argument to your function.
# You are not responsible for reading any input from stdin.


# Output Format

# If the list contains a cycle, your function must return true.
# If the list does not contain a cycle, it must return false.
# The binary integer corresponding to the boolean value returned by your function is printed to stdout
# by our hidden code checker.


"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


#https://stackoverflow.com/questions/20353835/fastest-way-to-prove-linked-list-is-circular-in-python
def is_circular(head):
    slow = head
    fast = head

    while fast != None:
        slow = slow.next

        if fast.next != None:
            fast = fast.next.next
        else:
            return False

        if slow is fast:
            return True

    return False

def has_cycle(head):
    if head.next is None:
        return False
    else:
        a = []
        node = head
        while (not node.next is None) or (not node.next.data in a):
            a.append(node.data)
            if node.next.data in a:
                return True
            node = node.next
    return False