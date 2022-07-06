//
//  Solution.swift
//  Counting Bits
//
//  Created by 송태환 on 2022/03/17.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/counting-bits/)
class Solution {
    func countBits(_ n: Int) -> [Int] {
        return (0...n).map { $0.nonzeroBitCount }
    }
}
