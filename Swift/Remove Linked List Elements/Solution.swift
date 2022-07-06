//
//  Solution.swift
//  Remove Linked List Elements
//
//  Created by 송태환 on 2022/04/07.
//

import Foundation

class Solution {
    /// Recursive
    /// Termination 상황에서 제일 마지막 노드에서 부터 Head 를 향해가면서 각 노드의 next 에 nil 또는 이전 노드 할당
    func removeElements2(_ head: ListNode?, _ val: Int) -> ListNode? {
        guard let head = head else { return nil }
        head.next = removeElements(head.next, val)
        return head.val == val ? head.next : head
    }
    
    /// Iteration
    func removeElements(_ head: ListNode?, _ val: Int) -> ListNode? {
        var newHead = head
        
        while newHead != nil && newHead?.val == val {
            newHead = newHead?.next
        }
        
        var node = newHead
        
        while node != nil {
            if node?.next?.val == val {
                node?.next = node?.next?.next
            } else {
                node = node?.next
            }
        }
        
        return newHead
    }
}
