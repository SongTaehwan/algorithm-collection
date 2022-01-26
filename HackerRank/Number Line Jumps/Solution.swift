//
//  Solution.swift
//  Number Line Jumps
//
//  Created by 송태환 on 2022/01/26.
//

import Foundation

/// [Check out problem](https://www.hackerrank.com/challenges/kangaroo/problem)
func kangaroo(x1: Int, v1: Int, x2: Int, v2: Int) -> String {
    if (x1 > x2 && v1 >= v2) || (x1 < x2 && v1 <= v2) {
        return "NO"
    }

    var k1 = x1
    var k2 = x2
    
    var distance = max(k1 - k2, k2 - k1)
    
    while k1 != k2 {
        k1 += v1
        k2 += v2
        
        let remaining = max(k1 - k2, k2 - k1)
        
        if remaining > distance {
            return "NO"
        }
        
        distance = remaining
    }
    
    return "YES"
}
