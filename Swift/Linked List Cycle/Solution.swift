//
//  Solution.swift
//  Linked List Cycle
//
//  Created by 송태환 on 2022/01/13.
//

import Foundation

class Solution: Utility {
    func hasCycle(_ head: ListNode?) -> Bool {
        var fast = head
        var slow = head
        
        while let next = fast?.next {
            fast = next.next
            slow = slow?.next
            
            if (fast === slow) {
                return true
            }
        }
        
        return false
    }
}
