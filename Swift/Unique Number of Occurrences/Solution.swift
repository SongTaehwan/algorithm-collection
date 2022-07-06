//
//  Solution.swift
//  Unique Number of Occurrences
//
//  Created by 송태환 on 2022/02/16.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/unique-number-of-occurrences/)
class Solution {
    func uniqueOccurrences(_ arr: [Int]) -> Bool {
        let dict = arr.reduce(into: [Int:Int]()) { $0[$1, default: 0] += 1 }
        var pointer = 0
        
        return dict.values.sorted().allSatisfy {
            if pointer < $0 {
                pointer = $0
                return true
            }
            
            return false
        }
    }
}
