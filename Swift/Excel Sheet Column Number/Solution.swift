//
//  Solution.swift
//  Excel Sheet Column Number
//
//  Created by 송태환 on 2022/02/22.
//

import Foundation

/// [Check out the problem]](https://leetcode.com/problems/excel-sheet-column-number/)
class Solution {
    func titleToNumber(_ columnTitle: String) -> Int {
        var result = 0
        
        for char in columnTitle {
            result = result * 26 + Int(char.asciiValue! - Character("A").asciiValue!) + 1
        }
        
        return result
    }
}
