//
//  solution.swift
//  algorithms
//
//  Created by 송태환 on 2022/01/13.
//

import Foundation

class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        guard x >= 0 else { return false }
        
        var result = 0
        var y = x
        
        while y > 0 {
            result *= 10
            result += y % 10
            y /= 10
        }
        
        return result == x
    }
    
    func isPalindrome2(_ x: Int) -> Bool {
        let chars = String(x).map { String($0) }
        let reversed = chars.reversed().joined()
        let result = Int(reversed)
        return result != nil ? result == x : false
    }
}
