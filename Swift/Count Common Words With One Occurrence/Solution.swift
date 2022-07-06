//
//  Solution.swift
//  Count Common Words With One Occurrence
//
//  Created by 송태환 on 2022/04/04.
//

import Foundation

class Solution {
    func countWords(_ words1: [String], _ words2: [String]) -> Int {
        var checker = Set<String>()
        var dict = words1.reduce(into: [String:Int]()) {
            if !checker.contains($1) {
                checker.update(with: $1)
                $0[$1, default: 0] += 1
            } else {
                $0.removeValue(forKey: $1)
            }
        }
        
        for word in words2 {
            if dict[word] != nil {
                dict[word, default: 0] += 1
            }
        }
        
        return dict.filter { $0.value == 2 }.count
    }
}
