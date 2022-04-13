//
//  Solution.swift
//  Calculate Money in Leetcode Bank
//
//  Created by 송태환 on 2022/04/13.
//

import Foundation

/// [Checkout the problem](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)
class Solution {
    func totalMoney(_ n: Int) -> Int {
        guard n != 1 else { return 1 }
        
        var extra = 0
        var saving = 1
        
        for i in 2...n {
            
            if i % 7 == 1 {
                extra += 1
            }
            
            if i % 7 == 0 {
                saving += 7
            }
            
            saving += (i % 7) + extra
        }
        
        return saving
    }
    
    func refactor(_ n: Int) -> Int {
        var savings = 0
        
        for i in 0..<n {
            let day = (i % 7) + 1
            let week = i / 7
            savings += day + week
        }
        
        return savings
    }
}
