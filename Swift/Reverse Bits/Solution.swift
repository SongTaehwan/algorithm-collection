//
//  Solution.swift
//  Reverse Bits
//
//  Created by 송태환 on 2022/01/19.
//

import Foundation

class Solution {
    func reverseBits(_ n: Int) -> Int {
        var binary = n
        var result = 0
        
        while binary > 0 {
            result *= 10
            result += binary % 10
            binary /= 10
        }
        
        return result
    }
}
