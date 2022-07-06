//
//  Solution.swift
//  Majority Element
//
//  Created by 송태환 on 2022/04/06.
//

import Foundation

/// [Checkout the problem](https://leetcode.com/problems/majority-element/)
/// [Boyer-Moore Majority Vote Algorithm](https://www.cs.utexas.edu/~moore/best-ideas/mjrty/)
class Solution {
    func majorityElement2(_ nums: [Int]) -> Int {
        var sortedNumbers = nums.sorted()
        var pointer = sortedNumbers.removeLast()
        var count = 1
        let criteria = nums.count / 2 + nums.count & 1
        
        while sortedNumbers.count != 0 {
            let number = sortedNumbers.removeLast()
            
            if number != pointer {
                pointer = number
                count = 1
                continue
            }
            
            count += 1
            
            if count >= criteria {
                return number
            }
        }
        
        return pointer
    }
    
    /// Boyer-Moore Majority Vote Algorithm
    func majorityElement(_ nums: [Int]) -> Int {
        var count = 1, number = nums[0]
        
        for i in 1..<nums.count {
            if count == 0 {
                count += 1
                number = nums[i]
            } else if number == nums[i] {
                count += 1
            } else {
                count -= 1
            }
        }
        
        return number
    }
    
}
