//
//  Solution.swift
//  Counting Words With a Given Prefix
//
//  Created by 송태환 on 2022/04/05.
//

import Foundation

/// [Checkout the problem](https://leetcode.com/problems/counting-words-with-a-given-prefix/)
class Solution {
    func prefixCount(_ words: [String], _ pref: String) -> Int {
        var count = 0
        
        for word in words {
            if word.hasPrefix(pref) {
                count += 1
            }
        }
        
        return count
    }
}
