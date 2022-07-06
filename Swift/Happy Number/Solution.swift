//
//  Solution.swift
//  Happy Number
//
//  Created by 송태환 on 2022/04/20.
//

import Foundation

/// [Checkout the problem](https://leetcode.com/problems/happy-number/)
class Solution {
    // FIXME: 터미네이션 조건 찾기
    func isHappy(_ n: Int) -> Bool {
        guard n != 1 else { return true }

        var result = 0
        var number = n
        
        while number > 0 {
            let num = number % 10
            number /= 10
            result += num * num
        }
        
        return isHappy(result)
    }
}
