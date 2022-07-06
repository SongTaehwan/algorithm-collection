//
//  Solution.swift
//  Merge Strings Alternately
//
//  Created by 송태환 on 2022/01/27.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/merge-strings-alternately/)
class Solution {
    func mergeAlternately(_ word1: String, _ word2: String) -> String {
        var result = ""
        
        for i in 0..<max(word1.count, word2.count) {
            let char1 = word1.count > i ? String(word1[word1.index(word1.startIndex, offsetBy: i)]) : ""
            let char2 = word2.count > i ? String(word2[word2.index(word2.startIndex, offsetBy: i)]) : ""
            result += char1
            result += char2
        }

        return result
    }
    
    // Two Pointer
    func refactor(_ word1: String, _ word2: String) -> String {
        let l1 = word1.count, l2 = word2.count
        var i = 0, j = 0
        
        var result = ""
        
        while i < l1 || j < l2 {
            if i < l1 {
                result += String(word1[word1.index(word1.startIndex, offsetBy: i)])
                i += 1
            }
            
            if j < l2 {
                result += String(word2[word2.index(word2.startIndex, offsetBy: j)])
                j += 1
            }
        }
        
        return result
    }
}
