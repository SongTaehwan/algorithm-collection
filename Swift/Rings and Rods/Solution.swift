//
//  Solution.swift
//  Rings and Rods
//
//  Created by 송태환 on 2022/02/02.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/rings-and-rods/)
class Solution {
    func countPoints(_ rings: String) -> Int {
        var dict = [Character:Set<Character>]()
        let chars = rings.map { $0 }
        
        for i in stride(from: 0, through: rings.count-1, by: 2) {
            let color = chars[i]
            let rod = chars[i+1]
            
            dict[rod, default: Set()].insert(color)
        }
        
        return dict.filter { $0.value.count == 3 }.count
    }
    
    func refactor(_ rings: String) -> Int {
        let c = rings.count
        var rods = [Int](repeating: 0, count: 10)
        
        for index in stride(from: 0, to: c, by: 2) {
            let colorBit = rings[index] == "R" ? 1 : (rings[index] == "G" ? 2 : 4)
            let rod: Int = rings[index + 1].wholeNumberValue!
            rods[rod] = rods[rod] | colorBit
        }
        
        return rods.reduce(into: 0) { $0 += $1 == 7 ? 1 : 0 }
    }
}

extension String {
    subscript(index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
