# 369. Plus One Linked List
'''
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        digit, copy = 0, head
        while copy:
            digit = digit*10 + copy.val
            copy = copy.next
        digit += 1
        
        ans_head = temp = ListNode(0)
        for ch in str(digit):
            temp.next = ListNode(int(ch))
            temp = temp.next
        return ans_head.next
        
        

