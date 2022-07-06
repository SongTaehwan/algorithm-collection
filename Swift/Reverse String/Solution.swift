//
//  Solution.swift
//  Reverse String
//
//  Created by 송태환 on 2022/02/10.
//

import Foundation

class Solution {
    func reverseString(_ s: inout [Character]) {
        var p1 = Character(" ")
        var p2 = Character(" ")
        
        for i in 0..<s.count/2 {
            p1 = s[i]
            p2 = s[s.count - 1 - i]
            s[i] = p2
            s[s.count-1-i] = p1
        }
    }
    
    // Built-in
    func refactor1(_ s: inout [Character]) {
        s.reverse() // reverse not reversed
    }
        
    // Built-in
    func refactor2(_ s: inout [Character]) {
        var index = s.count - 1
        
        for i in 0..<s.count / 2 {
            s.swapAt(i, index)
            index -= 1
        }
    }
    
}
