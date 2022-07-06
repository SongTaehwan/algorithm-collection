//
//  Solution.swift
//  Middle of the Linked List
//
//  Created by 송태환 on 2022/04/08.
//

import Foundation

/// [Checkout the problem](https://leetcode.com/problems/middle-of-the-linked-list/)
class Solution {
    func middleNode(_ head: ListNode?) -> ListNode? {
        guard var node = head, head?.next != nil else { return head }
        var nodes = [head]
        
        while let next = node.next {
            nodes.append(next)
            node = next
        }
        
        let middle = nodes.count / 2
        
        return nodes[middle]
    }
    
    /// Two Pointer 중간 위치 찾는 알고리즘
    /// pointer 1 - 1칸씩 이동, pointer 2 - 2칸씩 이동
    //  pointer 1 / 2
    //    1 / 1
    //    2 / 3
    //    3 / 5
    //    4 / 7
    //    5 / 9
    //    6 / 11
    //    7 / 13
    func refactor(_ head: ListNode?) -> ListNode? {
        var head = head
        var temp = head
        
        while temp != nil && temp?.next != nil {
            head = head?.next
            temp = temp?.next?.next
        }
        
        return head
    }
}
