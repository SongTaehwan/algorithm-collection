//
//  solution.swift
//  Reserve Integer
//
//  Created by 송태환 on 2022/01/13.
//

import Foundation

class Solution {
    func reverse(_ x: Int) -> Int {
        var y = x
        var count = 1
        
        while y >= 10 || y <= -10 {
            y /= 10
            count *= 10
        }
        
        y = x
        var result = 0
        
        while y != 0 {
            let modular = y % 10
            result += modular * count
            
            if result > Int32.max || result < Int32.min {
                return 0
            }
            
            y /= 10
            count /= 10
        }
        
        return result
    }
    
    func refactoredReverse(_ x: Int) -> Int {
        var y = x
        var result = 0
        
        while y != 0 {
            result *= 10
            result += y % 10
            
            if result > Int32.max || result < Int32.min {
                return 0
            }
            
            y /= 10
        }
        
        return result
    }
}
