//
//  solution.swift
//  Remove Duplicates from Sorted List
//
//  Created by 송태환 on 2022/01/13.
//

import Foundation

class Solution: Utility {
    func deleteDuplicates(_ head: ListNode?) -> ListNode? {
        var node = head
        
        while let next = node?.next {
            if node?.val == next.val {
                node!.next = next.next
            } else {
                node = next
            }
        }
        
        return head
    }
    
    // Hash Map
    func deleteDuplicatesWithHashMap(_ head: ListNode?) -> ListNode? {
        var dict = [Int: Bool]()
        var previousNode: ListNode? = nil
        var node = head
        
        while node != nil {
            let next = node!.next
            
            if dict[node!.val, default: false] {
                previousNode?.next = next
                node = next
                continue
            }
            
            dict[node!.val] = true
            previousNode = node
            node = next
        }
        
        return head
    }
}
