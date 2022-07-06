//
//  Solution.swift
//  Single Number
//
//  Created by 송태환 on 2022/02/09.
//

import Foundation

class Solution {
    func singleNumber(_ nums: [Int]) -> Int {
        var result = 0
        
        for num in nums {
            result ^= num
        }
        
        return result
    }
    
    func refactor(_ nums: [Int]) -> Int {
        return nums.reduce(0) { $0 ^ $1 }
    }
}
