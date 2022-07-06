//
//  Solution.swift
//  Number of Strings That Appear as Substrings in Word
//
//  Created by 송태환 on 2022/03/31.
//

import Foundation

class Solution {
    func numOfStrings2(_ patterns: [String], _ word: String) -> Int {
        var count = 0
        
        for char in patterns {
            if word.contains(char) {
                count += 1
            }
        }
        
        return count
    }
    
    func numOfStrings(_ patterns: [String], _ word: String) -> Int {
        return patterns.reduce(0) { word.contains($1) ? $0 + 1 : $0 }
    }
}
