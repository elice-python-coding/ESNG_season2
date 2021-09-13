def isPalindrom(self, head:ListNode)->bool:
    q : Deque = collections.deque()

    if not head:
        return True
    
    node = head
    while node is None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True