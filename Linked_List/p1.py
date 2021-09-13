def isPalindrome(self,head:List) -> bool:
    q = []

    if not head:
        return True
    
    node = head

    while node is not None:
        q.append(node.val)
        node = node.next 

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True
