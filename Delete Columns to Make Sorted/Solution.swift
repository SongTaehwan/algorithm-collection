//
//  Solution.swift
//  Delete Columns to Make Sorted
//
//  Created by 송태환 on 2022/02/25.
//

import Foundation

/// [Check out the problem]](https://leetcode.com/problems/delete-columns-to-make-sorted/)
class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        let nums = strs.map { $0.compactMap { $0.asciiValue } }
        let column = nums.first?.count ?? 0
        let row = nums.count
        
        var currentRow = 0
        var currentColumn = 0
        var result = 0
        var previousValue = 0
        
        while currentRow < row && currentColumn < column {
            let value = Int(nums[currentRow][currentColumn])
            
            if previousValue > value {
                previousValue = 0
                result += 1
                currentRow = 0
                currentColumn += 1
                continue
            }
            
            previousValue = value
            currentRow += 1
            
            if currentRow == row && currentColumn < column {
                previousValue = 0
                currentRow = 0
                currentColumn += 1
            }
        }
        
        
        return result
    }
}
