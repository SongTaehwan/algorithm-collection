//
//  Solution.swift
//  Minimum Sum of Four Digit Number After Splitting Digits
//
//  Created by 송태환 on 2022/03/09.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/)
class Solution {
    func minimumSum(_ num: Int) -> Int {
        var num = num
        var numbers = [Int]()
        
        while num > 0 {
            numbers.append(num % 10)
            num /= 10
        }
        
        var nums = numbers.sorted { $0 > $1 }
        return nums.removeLast() * 10 + nums.removeLast() * 10 + nums.removeLast() + nums.removeLast()
    }
}

