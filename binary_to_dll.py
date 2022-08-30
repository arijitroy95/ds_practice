"""
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place.
The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL.
The order of nodes in DLL must be same as Inorder of the given Binary Tree.
The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.
"""
from collections import deque
import sys


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def build_tree(s):
    if len(s) == 0 or s[0] == "N":
        return None
    ip = list(map(str, s.strip().split()))
    root = Node(int(ip[0]))
    size = 0
    q = deque()
    q.append(root)
    size += 1
    i = 1
    while size > 0 and i < len(ip):
        cur_node = q[0]
        q.popleft()
        size -= 1
        cur_val = ip[i]
        if cur_val != 'N':
            cur_node.left = Node(int(cur_val))
            q.append(cur_node.left)
            size += 1
        i += 1
        if i >= len(ip):
            break
        cur_val = ip[i]
        if cur_val != 'N':
            cur_node.right = Node(int(cur_val))
            q.append(cur_node.right)
            size += 1
        i += 1
    return root


prev_node = None


# Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self, root):
        if root is None:
            return root
        head = self.bToDLL(root.left)
        global prev_node
        if prev_node is None:
            head = root
        else:
            root.left = prev_node
            prev_node.right = root

        prev_node = root
        self.bToDLL(root.right)
        return head


def print_dll(head):
    prev = None
    sys.stdout.flush()
    while head is not None:
        print(head.data, end=' ')
        prev = head
        head = head.right
    print()
    while prev is not None:
        print(prev.data, end=' ')
        prev = prev.left
    print()


s = "1 3 10 5 7 9 N 5 5 9 2 10"
root = build_tree(s)
obj = Solution()
root = obj.bToDLL(root)
print_dll(root)