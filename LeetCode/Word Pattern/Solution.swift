//
//  Solution.swift
//  Word Pattern
//
//  Created by 송태환 on 2022/01/17.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/word-pattern/)
class Solution {
    func wordPattern(_ pattern: String, _ s: String) -> Bool {
        var wordToPattern = [String: Character]()
        var patternToWord = [Character: String]()
        let words = s.components(separatedBy: .whitespaces)
        
        guard pattern.count == words.count else { return false }

        for (i, pattern) in pattern.enumerated() {
            let word = words[i]
            
            if let matchingPattern = wordToPattern[word], matchingPattern != pattern {
                return false
            }
            
            if let matchingWord = patternToWord[pattern], matchingWord != word {
                return false
            }
            
            wordToPattern[word] = pattern
            patternToWord[pattern] = word
        }
        
        return true
    }
}
