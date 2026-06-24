class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


def build(values: list) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def to_list(head: Optional[ListNode]) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        
        temp = second
        prev = None
        while temp:
            temp_next = temp.next
            temp.next = prev
            prev = temp
            temp = temp_next
        
        dummy = ListNode()
        curr = dummy
        
        while head and prev:
            curr.next = head
            curr = head
            head = head.next
            curr.next = prev
            curr = prev
            prev = prev.next
        
        if head:
            curr.next = head
            curr = head
            head = head.next
        
        if prev:
            curr.next = prev
            curr = prev
            prev = prev.next
            
        return dummy.next
        

# --- tests ---
sol = Solution()

head = build([1, 2, 3, 4, 5])
sol.reorderList(head)
print(to_list(head))  # expected: [1, 5, 2, 4, 3]

head = build([1, 2, 3, 4])
sol.reorderList(head)
print(to_list(head))  # expected: [1, 4, 2, 3]
