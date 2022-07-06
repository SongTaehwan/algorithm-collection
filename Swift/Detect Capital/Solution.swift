//
//  Solution.swift
//  Detect Capital
//
//  Created by 송태환 on 2022/01/24.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/detect-capital/)
class Solution {
    func detectCapitalUse(_ word: String) -> Bool {
        var count = 0
        let firstCharIsUppercased = word.first!.isUppercase
        
        for char in word {
            if char.isUppercase {
                count += 1
            }
            
            if !firstCharIsUppercased && count > 0 {
                return false
            }
        }
        
        return count == word.count || count <= 1
    }
}
