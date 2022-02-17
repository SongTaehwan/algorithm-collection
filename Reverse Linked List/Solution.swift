//
//  Solution.swift
//  Reverse Linked List
//
//  Created by 송태환 on 2022/02/17.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/reverse-linked-list/)
class Solution {
    func reverseList1(_ head: ListNode?) -> ListNode? {
        var node = head
        var result = [Int]()
        
        while node != nil {
            result.append(node!.val)
            node = node?.next
        }
        
        node = head
        
        for num in result.reversed() {
            print(num)
            node!.val = num
            node = node?.next
        }
        
        return head
    }
    
    // iteration
    func reverseList2(_ head: ListNode?) -> ListNode? {
        var node = head
        var prev: ListNode? = nil
        
        while node != nil {
            let next = node?.next
            node?.next = prev
            prev = node
            node = next
        }
        
        return prev
    }
    
    // recursive
    func reverseList(_ head: ListNode?) -> ListNode? {
        return recursive(head, nil)
    }
    
    func recursive(_ prevHead: ListNode?, _ newHead: ListNode?) -> ListNode? {
        guard let head = prevHead else { return newHead }
        let next = head.next
        head.next = newHead
        return recursive(next, head)
    }
    
}
