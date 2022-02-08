//
//  Solution.swift
//  Add Digits
//
//  Created by 송태환 on 2022/02/08.
//

import Foundation

/// [Check out problem](https://leetcode.com/problems/add-digits/)
class Solution {
    func addDigits(_ num: Int) -> Int {
        let number = num / 10 + num % 10
        
        if number >= 10 {
            return addDigits(number)
        }
        
        return number
    }
    
    func addDigits2(_ num: Int) -> Int {
        var result = num
        
        while result >= 10 {
            result = result / 10 + result % 10
        }
        
        return result
    }
    
    func refactor(_ num: Int) -> Int {
        return 1 + (num - 1) % 9
    }
    
}
