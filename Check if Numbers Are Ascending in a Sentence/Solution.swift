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
    
    func refactor(_ s: String) -> Bool {
        let nums = s.split(separator: " ").compactMap { Int($0) }
        
        // zip(nums, nums.dropFirst())
        // 길이를 마추기 위해 남는 아이템은 자름
        // 1,3,4,6,12 --> 12 제거
        // 3,4,6,12
        return zip(nums, nums.dropFirst()).allSatisfy { $0 < $1 }
    }
}
