//
//  Solution.swift
//  Number of 1 Bits
//
//  Created by 송태환 on 2022/03/17.
//

import Foundation

class Solution {
    func hammingWeight(_ n: Int) -> Int {
        var result = 0
        var num = n
        
        while num > 0 {
            if num % 2 == 1 {
                result += 1
            }
            
            num = num / 2
            
        }
        
        return result
    }
    
    //simple
    func hammingWeight2(_ n: Int) -> Int {
        return n.nonzeroBitCount
    }
    
    func refactor(_ n: Int) -> Int {
        var count = 0
        var num = n
        
        while num > 0 {
            num &= (num - 1)
            count += 1
        }
        
        return count
    }
}
