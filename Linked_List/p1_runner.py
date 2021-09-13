def isPalinedrome(self, head:ListNode)->bool:
    rev = None
    slow = fast = head #slow와 fast모두 head부터 시작
    while fast and fast.next:
        fast = fast.next.next #fast는 next의next
        rev, rev.next, slow = slow, rev, slow.next ##rev는 slow, rev.next는 rev(slow.next를 rev), slow는 slow.next
    
    if fast:
        slow = slow.next
    
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev