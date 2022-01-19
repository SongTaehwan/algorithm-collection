//
//  Solution.swift
//  Convert Binary Number in a Linked List to Integer
//
//  Created by 송태환 on 2022/01/13.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)
class Solution: Utility {
    func getDecimalValue(_ head: ListNode?) -> Int {
        var numbers = [Int]()
        var result = 0
        var node = head
        var count = 0
        
        while node != nil {
            numbers.append(node!.val)
            node = node!.next
            count += 1
        }
        
        for number in numbers {
            count -= 1
            result += (number << count)
        }
        
        return result
    }
    
    func refactored(_ head: ListNode?) -> Int {
        var result = 0
        var node = head
        // 1101
        // 1 -> 11 -> 110 -> 1101
        while node != nil {
            result = (result << 1) | node!.val
            node = node!.next
        }
        
        return result
    }
}
