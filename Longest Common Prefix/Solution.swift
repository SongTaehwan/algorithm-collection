//
//  Solution.swift
//  Longest Common Prefix
//
//  Created by 송태환 on 2022/01/13.
//

import Foundation

class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        var prefix = strs[0]
        
        for word in strs {
            while !word.hasPrefix(prefix) {
                prefix = String(prefix.dropLast())
            }
        }
        
        return prefix
    }
}
