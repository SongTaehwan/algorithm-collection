//
//  Solution.swift
//  Replace All Digits with Characters
//
//  Created by 송태환 on 2022/01/24.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/replace-all-digits-with-characters/)
class Solution {
    func replaceDigits(_ s: String) -> String {
        var result = ""
        var asciiValue = UInt8(0)
        
        for (i, char) in s.enumerated() {
            var value = String(char)
            
            if i % 2 == 0 {
                asciiValue = char.asciiValue!
            } else {
                value = String(UnicodeScalar(asciiValue + UInt8(value)!))
            }
            
            result += value
        }
        
        return result
    }
}
