//
//  Solution.swift
//  Sum of Unique Elements
//
//  Created by 송태환 on 2022/04/04.
//

import Foundation

/// [Checkout the problem](https://leetcode.com/problems/sum-of-unique-elements/submissions/)
class Solution {
    func sumOfUnique(_ nums: [Int]) -> Int {
        let dict = nums.reduce(into: [Int: Int]()) { $0[$1, default: 0] += 1 }
        return dict.filter { $0.value == 1 }.keys.reduce(0, +)
    }
}
