//
//  Solution.swift
//  Matrix Diagonal Sum
//
//  Created by 송태환 on 2022/01/28.
//

import Foundation

/// [Checkout the problem](https://leetcode.com/problems/matrix-diagonal-sum/)
class Solution {
    func diagonalSum(_ mat: [[Int]]) -> Int {
        var result = 0
        let last = mat.count-1
        
        for (i, row) in mat.enumerated() {
            result += row[i]
            
            if i != last-i {
                result += row[last - i]
            }
            
        }
        
        return result
    }
    
    func refactor(_ mat: [[Int]]) -> Int {
        var result = 0
        let len = mat.count-1
        
        for (i, row) in mat.enumerated() {
            result += (row[i] + row[len - i])
        }
        
        if len % 2 == 0 {
            let mid = len/2
            result -= mat[mid][mid]
        }
        
        return result
    }
}
