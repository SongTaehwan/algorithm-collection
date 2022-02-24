//
//  Solution.swift
//  Check if Numbers Are Ascending in a Sentence
//
//  Created by 송태환 on 2022/02/24.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/)
class Solution {
    func areNumbersAscending(_ s: String) -> Bool {
        let nums = s.components(separatedBy: " ").compactMap { Int($0) }
        var result = 0
        
        for num in nums {
            if result < num {
                result = num
            } else {
                return false
            }
        }
        
        return true
    }
}
