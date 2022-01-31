//
//  Solution.swift
//  Richest Customer Wealth
//
//  Created by 송태환 on 2022/01/31.
//

import Foundation

/// [Check out the problem](https://leetcode.com/problems/richest-customer-wealth/)
class Solution {
    func maximumWealth(_ accounts: [[Int]]) -> Int {
        var result = 0
        
        for account in accounts {
            result = max(result, account.reduce(0, +))
        }
        
        return result
    }
    
    func refactor(_ accounts: [[Int]]) -> Int {
        return accounts.map { $0.reduce(0, +) }.max()!
    }
}
