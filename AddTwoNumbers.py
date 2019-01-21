"""
https://leetcode.com/problems/add-two-numbers/
Level: Medium
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2, next_place=0):

    if l1==None:
        if l2==None:
            if next_place==0:
                this_node = None
            else:
                this_node = ListNode(next_place)
        else:
            sum = next_place + l2.val
            this_node = ListNode(sum % 10)
            this_node.next = addTwoNumbers(None, l2.next, sum // 10)
    elif l2==None:
        sum = next_place + l1.val
        this_node = ListNode(sum%10)
        this_node.next = addTwoNumbers(None, l1.next, sum // 10)
    else:
        sum = next_place + l1.val +l2.val
        this_node = ListNode(sum % 10)
        this_node.next = addTwoNumbers(l1.next, l2.next, sum // 10)
    return this_node

def printList(listNode):
    print(listNode.val)
    if(listNode.next != None):
        printList(listNode.next)

l1 = ListNode(2)
l1Second = ListNode(4)
l1Third = ListNode(3)
l1.next = l1Second
l1Third.next = l1Second

l2 = ListNode(5)
l2Second = ListNode(6)
l2Third = ListNode(4)
l2.next = l2Second
l2Third.next = l2Second

outputList = addTwoNumbers(l1, l2, 0)

printList(outputList)
