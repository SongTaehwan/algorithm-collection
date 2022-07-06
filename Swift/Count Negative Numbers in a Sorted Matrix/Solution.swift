//
//  Solution.swift
//  Count Negative Numbers in a Sorted Matrix
//
//  Created by 송태환 on 2022/02/04.
//

import Foundation

// ++++++
// ++++--
// ++++--
// +++---
// +-----
// +-----
/// [Check out the problem](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)
class Solution {
    func countNegatives(_ grid: [[Int]]) -> Int {
        return grid.flatMap { $0 }.sorted().reduce(0) { $1 < 0 ? $0 + 1 : $0 }
    }
    
    func refactor(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var row = 0, index = n - 1, count = 0
        
        while row < m && index >= 0 {
            if grid[row][index] < 0 {
                index -= 1
                count += m - row
            } else {
                row += 1
            }
        }
            
        return count
    }
}
