//
//  Solution.swift
//  Binary Search
//
//  Created by 송태환 on 2022/01/14.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/binary-search/)
class Solution: Utility {
    /// Using Array
    func search(_ nums: [Int], _ target: Int) -> Int {
        for (i, num) in nums.enumerated() {
            if num == target {
                return i
            }
        }

        return -1
    }
    
    /// Using Binary Search
    func refactored(_ nums: [Int], _ target: Int) -> Int {
        var mid = (nums.count - 1) / 2
        let direction = nums[mid] > target ? "left" : "right"
        
        while mid >= 0 && mid < nums.count {
            guard nums[mid] != target else { return mid }
            
            if direction == "left" {
                mid -= 1
            } else {
                mid += 1
            }
        }
        
        return -1
    }
    
    // Better
    func better(_ nums: [Int], _ target: Int) -> Int {
        var left = 0, right = nums.count - 1
        
        while left <= right {
            let mid = (left + right) / 2

            guard nums[mid] != target else { return mid }
            
            if nums[mid] < target {
                left += 1
            } else {
                right -= 1
            }
        }
        
        return -1
    }
}
