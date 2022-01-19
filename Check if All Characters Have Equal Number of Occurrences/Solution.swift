//
//  Solution.swift
//  Check if All Characters Have Equal Number of Occurrences
//
//  Created by 송태환 on 2022/01/20.
//

import Foundation

class Solution {
    // Original
    func areOccurrencesEqual(_ s: String) -> Bool {
        var dict = [Character: Int]()
        
        for char in s {
            dict[char, default: 0] += 1
        }
        
        let maxValue = dict.values.max()
        return dict.values.filter { $0 != maxValue }.count == 0
    }
    
    func refactored(_ s: String) -> Bool {
        let dict = s.reduce(into: [Character: Int]()) { $0[$1, default: 0] += 1 }
        return dict.values.allSatisfy { $0 == dict.values.first }
    }
}
